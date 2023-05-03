"""FUGLE PYTHON API FORWARDER"""


import os
import time

from prometheus_client import start_http_server

from env import RequiredEnv
from fugle import Fugle
from grpcsrv import GRPCServer
from logger import logger
from rabbitmq import RabbitMQS
from rabbitmq_setting import RabbitMQSetting

if __name__ == "__main__":
    env = RequiredEnv()

    PROMETHEUS_PORT = 8888
    start_http_server(PROMETHEUS_PORT)
    logger.info("fugle prometheus server started at port %d", PROMETHEUS_PORT)

    try:
        rc = RabbitMQSetting(
            env.rabbitmq_user,
            env.rabbitmq_password,
            env.rabbitmq_host,
            env.rabbitmq_exchange,
        )
        rc.reset_rabbitmq_exchange()

    except RuntimeError:
        logger.error("reset rabbitmq exchange fail, retry after 30 seconds")
        time.sleep(30)
        os._exit(0)

    rabbit = RabbitMQS(
        env.rabbitmq_url,
        env.rabbitmq_exchange,
        8,
    )

    fugle = Fugle()
    sdk = fugle.get_sdk()

    @sdk.on("error")
    def on_error(err):
        logger.error("on_error: %s", err)

    @sdk.on("close")
    def on_close(websocket, close_status_code, close_msg):
        logger.error("ws type: %s", type(websocket))
        logger.error("close_status_code type: %s", type(close_status_code))
        logger.error("close_msg type: %s", type(close_msg))
        logger.error(websocket)
        logger.error(close_status_code)
        logger.error(close_msg)

    @sdk.on("order")
    def on_order(_):
        fugle.update_local_order()

    @sdk.on("dealt")
    def on_dealt(_):
        fugle.update_local_order()

    fugle.connect_websocket()

    try:
        server = GRPCServer(rabbit=rabbit, fugle=fugle)
        server.serve(port=env.grpc_port)

    except RuntimeError:
        logger.error("runtime error, retry after 30 seconds")
        time.sleep(30)
        os._exit(1)

    except KeyboardInterrupt:
        os._exit(0)
