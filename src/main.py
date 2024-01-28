"""FUGLE PYTHON API FORWARDER"""

import os
import time

from prometheus_client import start_http_server

from env import RequiredEnv
from fugle import Fugle
from grpcsrv.grpcsrv import GRPCServer
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

    try:
        server = GRPCServer(rabbit=rabbit, fugle=Fugle())
        server.serve(port=env.grpc_port)

    except Exception as e:
        logger.error(e)

    finally:
        logger.info("shutdown fugle")
        os._exit(0)
