import logging
import threading
import time
from queue import Queue

import pika

from logger import logger

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
        ch.exchange_declare(exchange=self.exchange, exchange_type="direct", durable=True)
        return PikaCC(conn, ch)

    def fill_pika_queue(self):
        for _ in range(self.pool_size):
            self.pika_queue.put(self.create_pika())
        threading.Thread(target=self.send_heartbeat).start()

    def event_callback(self):
        logger.info("event_callback")

    def order_status_callback(self):
        logger.info("order_status_callback")

    def stock_quote_callback_v1(self):
        logger.info("stock_quote_callback_v1")

    def future_quote_callback_v1(self):
        logger.info("future_quote_callback_v1")

    def stock_bid_ask_callback(self):
        logger.info("stock_bid_ask_callback")

    def future_bid_ask_callback(self):
        logger.info("future_bid_ask_callback")

    def send_order_arr(self):
        logger.info("send_order_arr")
