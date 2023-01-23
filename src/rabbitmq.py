import logging
import threading
import time
from datetime import datetime
from queue import Queue

import pika

import fugle_entity as fe
from pb import trade_pb2

logging.getLogger("pika").setLevel(logging.WARNING)


class PikaCC:
    def __init__(self, conn: pika.BlockingConnection, ch):
        self.conn = conn
        self.ch = ch

    def heartbeat(self):
        self.conn.process_data_events()


class RabbitMQS:
    def __init__(self, url: str, exchange: str, pool_size: int):
        # pika
        self.exchange = exchange
        self.parameters = pika.URLParameters(url)
        self.pool_size = pool_size
        # queue
        self.pika_queue: Queue = Queue()
        # lock
        self.order_cb_lock = threading.Lock()
        # initial connections
        self.fill_pika_queue()

    def send_heartbeat(self):
        while True:
            time.sleep(20)
            count = 0
            while True:
                if count >= self.pool_size:
                    break
                p = self.pika_queue.get(block=True)
                p.heartbeat()
                count += 1
                self.pika_queue.put(p)

    def create_pika(self):
        conn = pika.BlockingConnection(self.parameters)
        ch = conn.channel()
        ch.exchange_declare(
            exchange=self.exchange,
            exchange_type="direct",
            durable=True,
        )
        return PikaCC(conn, ch)

    def fill_pika_queue(self):
        for _ in range(self.pool_size):
            self.pika_queue.put(self.create_pika())
        threading.Thread(target=self.send_heartbeat).start()

    def send_order_arr(self, arr: list[fe.OrderResult]):
        if len(arr) == 0:
            return

        result = trade_pb2.OrderStatusArr()
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
                trade_pb2.OrderStatus(
                    code=order.stock_no,
                    action=str(order_action),
                    price=order.od_price,
                    quantity=order.mat_qty,
                    order_id=order.ord_no,
                    status=order.covert_to_OrderStatus().value,
                    order_time=datetime.strptime(
                        f"{order.ord_date} {order.ord_time[:-3]}",
                        "%Y%m%d %H%M%S",
                    ).strftime("%Y-%m-%d %H:%M:%S"),
                )
            )

        p = self.pika_queue.get(block=True)
        p.ch.basic_publish(
            exchange=self.exchange,
            routing_key="order_arr",
            body=result.SerializeToString(),
        )
        self.pika_queue.put(p)
