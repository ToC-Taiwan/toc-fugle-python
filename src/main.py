"""FUGLE PYTHON API FORWARDER"""
import os
import time

from prometheus_client import start_http_server

from cron import init_schedule_job
from env import RequiredEnv
from fugle import Fugle
from grpcsrv import serve
from logger import logger
from rabbitmq_setting import RabbitMQSetting

env = RequiredEnv()
grpc_port = env.grpc_port

start_http_server(8887)

# add schedule to exit the program
init_schedule_job()

# start rabbitmq container first
rc = RabbitMQSetting()
rc.reset_rabbitmq_exchange()

# login to fugle
Fugle()

try:
    serve(port=str(grpc_port), cfg=env)

except RuntimeError:
    logger.error("runtime error, retry after 30 seconds")
    time.sleep(30)
    os._exit(1)

except KeyboardInterrupt:
    os._exit(1)
