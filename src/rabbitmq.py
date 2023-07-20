import logging
import os
import threading
import time
from datetime import datetime
from queue import Queue

import pika
from pika.channel import Channel

import fugle_entity as fe
from logger import logger
from pb import mq_pb2

logging.getLogger("pika").setLevel(logging.WARNING)


class PikaCC:
    def __init__(self, conn: pika.BlockingConnection, channel: Channel):
        self.conn = conn
        self.channel = channel

    def heartbeat(self):
        self.conn.process_data_events()


class RabbitMQS:
    def __init__(self, url: str, exchange: str, pool_size: int):
        self.parameters = pika.URLParameters(url)
        self.exchange = exchange
        self.pool_size = pool_size

        # rabbit mq connection queue
        self.pika_queue: Queue = Queue()

        # initial connections
        self.fill_pika_queue()

        # lock
        self.order_cb_lock = threading.Lock()

        # subscribe terminate
        threading.Thread(target=self.subscribe_terminate, daemon=True).start()

    def subscribe_terminate(self):
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()

        result = channel.queue_declare(queue="", exclusive=True)
        # from https://www.rabbitmq.com/tutorials/tutorial-four-python.html
        # The queue_declare method returns a tuple of 3 values:
        # 1. queue name
        # 2. message count
        # 3. consumer count
        queue_name = result.method.queue
        channel.queue_bind(
            exchange=self.exchange,
            queue=queue_name,
            routing_key="terminate",
        )
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=self.terminate,
            auto_ack=True,
        )
        try:
            channel.start_consuming()
        except Exception as err:
            logger.error("subscribe_terminate error %s", err)

    def terminate(self, channel, method, properties, body):  # pylint: disable=unused-argument
        os._exit(0)

    def send_heartbeat(self):
        while True:
            time.sleep(20)
            count = 0
            while True:
                if count >= self.pool_size:
                    break
                rabbit = self.pika_queue.get(block=True)
                try:
                    rabbit.heartbeat()
                    count += 1
                except Exception as err:
                    logger.error("send_heartbeat error %s", err)
                self.pika_queue.put(rabbit)

    def create_pika(self):
        conn = pika.BlockingConnection(self.parameters)
        channel = conn.channel()
        channel.exchange_declare(
            exchange=self.exchange,
            exchange_type="direct",
            durable=True,
        )
        return PikaCC(conn, channel)

    def fill_pika_queue(self):
        for _ in range(self.pool_size):
            self.pika_queue.put(self.create_pika())
        threading.Thread(target=self.send_heartbeat, daemon=True).start()

    def send_order_arr(self, arr: list[fe.OrderResult]):
        if len(arr) == 0:
            return

        result = mq_pb2.OrderStatusArr()
        for order in arr:
            if order.err_msg != "":
                continue
            if order.buy_sell == "B":
                order_action = "Buy"
            elif order.buy_sell == "S":
                order_action = "Sell"
            else:
                continue

            result.data.append(
                mq_pb2.OrderStatus(
                    code=order.stock_no,
                    action=str(order_action),
                    price=order.od_price,
                    quantity=order.mat_qty,
                    order_id=order.ord_no,
                    status=order.covert_to_order_status().value,
                    order_time=datetime.strptime(
                        f"{order.ord_date} {order.ord_time[:-3]}",
                        "%Y%m%d %H%M%S",
                    ).strftime("%Y-%m-%d %H:%M:%S"),
                )
            )

        rabbit = self.pika_queue.get(block=True)
        try:
            rabbit.channel.basic_publish(
                exchange=self.exchange,
                routing_key="order_arr",
                body=result.SerializeToString(),
            )
        except Exception as err:
            logger.error("send_order_arr error %s", err)
        self.pika_queue.put(rabbit)
