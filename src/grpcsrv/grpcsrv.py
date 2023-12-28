from concurrent import futures

import grpc

from fugle import Fugle
from logger import logger
from pb import basic_pb2_grpc, trade_pb2_grpc
from rabbitmq import RabbitMQS

from .basic import RPCBasic
from .trade import RPCTrade


class GRPCServer:
    def __init__(self, rabbit: RabbitMQS, fugle: Fugle):
        basic_servicer = RPCBasic(fugle=fugle)
        trade_servicer = RPCTrade(rabbit=rabbit, fugle=fugle)
        server = grpc.server(
            futures.ThreadPoolExecutor(),
            options=[
                (
                    "grpc.max_send_message_length",
                    1024 * 1024 * 1024,
                ),
                (
                    "grpc.max_receive_message_length",
                    1024 * 1024 * 1024,
                ),
            ],
        )

        basic_pb2_grpc.add_BasicDataInterfaceServicer_to_server(basic_servicer, server)
        trade_pb2_grpc.add_TradeInterfaceServicer_to_server(trade_servicer, server)

        self.server = server

    def serve(self, port: str):
        self.server.add_insecure_port(f"[::]:{port}")
        self.server.start()
        logger.info("gRPC Server started at port %s", port)
        self.server.wait_for_termination()
