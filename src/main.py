"""FUGLE PYTHON API FORWARDER"""
import os
import time

from prometheus_client import start_http_server

from cron import init_schedule_job
from env import RequiredEnv
from fugle import Fugle
from grpcsrv import serve
from logger import logger
from rabbitmq import RabbitMQS
from rabbitmq_setting import RabbitMQSetting

env = RequiredEnv()
start_http_server(8887)

# add schedule to exit the program
init_schedule_job()

# start rabbitmq container first
rc = RabbitMQSetting()
rc.reset_rabbitmq_exchange()

rq = RabbitMQS(
    str(env.rabbitmq_url),
    str(env.rabbitmq_exchange),
    128,
)

fugle = Fugle()
sdk = fugle.get_sdk()


@sdk.on("error")
def on_error(err):
    rq.error_callback(err)


@sdk.on("order")
def on_order(data):
    rq.order_callback(data)


@sdk.on("dealt")
def on_dealt(data):
    rq.dealt_callback(data)


fugle.connect_websocket()

try:
    serve(port=str(env.grpc_port), rq=rq, f=fugle)

except RuntimeError:
    logger.error("runtime error, retry after 30 seconds")
    time.sleep(30)
    os._exit(1)

except KeyboardInterrupt:
    os._exit(1)
