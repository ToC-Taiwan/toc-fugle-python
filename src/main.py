"""FUGLE PYTHON API FORWARDER"""
from prometheus_client import start_http_server

from cron import init_schedule_job
from env import RequiredEnv
from rabbitmq_setting import RabbitMQSetting

env = RequiredEnv()
grpc_port = env.grpc_port

start_http_server(8887)

# add schedule to exit the program
init_schedule_job()

# start rabbitmq container first
rc = RabbitMQSetting()
rc.reset_rabbitmq_exchange()

# while True:
#     logger.info("FUGLE PYTHON API FORWARDER is running")
#     time.sleep(60)
#     pass
