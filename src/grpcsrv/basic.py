import os
import threading
import time

import google.protobuf.empty_pb2
import grpc

from fugle import Fugle
from logger import logger
from pb import basic_pb2_grpc


class RPCBasic(basic_pb2_grpc.BasicDataInterfaceServicer):
    def __init__(self, fugle: Fugle):
        self.fugle = fugle

    def CreateLongConnection(self, request_iterator, context: grpc.ServicerContext):
        logger.info("new fugle gRPC client connected")
        while context.is_active():
            time.sleep(1)
        os._exit(0)

    def Terminate(self, request, _):
        threading.Thread(target=self.wait_and_terminate, daemon=True).start()
        return google.protobuf.empty_pb2.Empty()

    def wait_and_terminate(self):
        time.sleep(3)
        os._exit(0)

    def Login(self, request, _):
        self.fugle.login()
        self.fugle.update_local_order()
        return google.protobuf.empty_pb2.Empty()
