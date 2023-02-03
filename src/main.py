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
start_http_server(8888)

# add schedule to exit the program
init_schedule_job()

# start rabbitmq container first
rc = RabbitMQSetting()
rc.reset_rabbitmq_exchange()

rabbit = RabbitMQS(
    str(env.rabbitmq_url),
    str(env.rabbitmq_exchange),
    128,
)

fugle = Fugle()
sdk = fugle.get_sdk()


@sdk.on("error")
def on_error(_):
    pass


@sdk.on("close")
def on_close(_):
    pass


@sdk.on("order")
def on_order(_):
    fugle.update_local_order()


@sdk.on("dealt")
def on_dealt(_):
    fugle.update_local_order()


fugle.connect_websocket()

try:
    serve(port=str(env.grpc_port), rabbit=rabbit, fugle=fugle)

except RuntimeError:
    logger.error("runtime error, retry after 30 seconds")
    time.sleep(30)
    os._exit(1)

except KeyboardInterrupt:
    os._exit(0)
