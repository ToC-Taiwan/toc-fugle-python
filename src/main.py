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
fugle = Fugle()

fugle.login()
fugle.show_cert()

# inventories = fugle.get_inventories()
# for inventory in inventories:
#     logger.info(json.dumps(inventory, indent=4))


# results = fugle.get_order_results()
# for result in results:
#     logger.info("ord_no: %s", result.ord_no)
#     logger.info("pre_ord_no: %s", result.pre_ord_no)
#     logger.info("stock_no: %s", result.stock_no)
#     logger.info("buy_sell: %s", result.buy_sell)
#     logger.info("ap_code: %s", result.ap_code)
#     logger.info("price_flag: %s", result.price_flag)
#     logger.info("trade: %s", result.trade)
#     logger.info("od_price: %.2f", result.od_price)
#     logger.info("org_qty: %d", result.org_qty)
#     logger.info("mat_qty: %d", result.mat_qty)
#     logger.info("cel_qty: %d", result.cel_qty)
#     logger.info("celable: %s", result.celable)
#     logger.info("err_code: %s", result.err_code)
#     logger.info("err_msg: %s", result.err_msg)
#     logger.info("avg_price: %.2f", result.avg_price)
#     logger.info("bs_flag: %s", result.bs_flag)
#     logger.info("org_qty_share: %d", result.org_qty_share)
#     logger.info("mat_qty_share: %d", result.mat_qty_share)
#     logger.info("cel_qty_share: %d", result.cel_qty_share)
#     logger.info("work_date: %s", result.work_date)
#     logger.info("ord_date: %s", result.ord_date)
#     logger.info("ord_time: %s", result.ord_time)
#     logger.info("ord_status: %s", result.ord_status)

try:
    serve(port=str(grpc_port), cfg=env)

except RuntimeError:
    logger.error("runtime error, retry after 30 seconds")
    time.sleep(30)
    os._exit(1)

except OSError as e:
    logger.error(e)
    os._exit(1)
