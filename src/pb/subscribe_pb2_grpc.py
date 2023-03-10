# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import entity_pb2 as entity__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import subscribe_pb2 as subscribe__pb2


class SubscribeDataInterfaceStub(object):
    """SubscribeDataInterface is the interface for subscribe data
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeStockTick = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/SubscribeStockTick',
                request_serializer=entity__pb2.StockNumArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockTick = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeStockTick',
                request_serializer=entity__pb2.StockNumArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.SubscribeStockBidAsk = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/SubscribeStockBidAsk',
                request_serializer=entity__pb2.StockNumArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockBidAsk = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeStockBidAsk',
                request_serializer=entity__pb2.StockNumArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.SubscribeFutureTick = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/SubscribeFutureTick',
                request_serializer=entity__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeFutureTick = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeFutureTick',
                request_serializer=entity__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.SubscribeFutureBidAsk = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/SubscribeFutureBidAsk',
                request_serializer=entity__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeFutureBidAsk = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeFutureBidAsk',
                request_serializer=entity__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=subscribe__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeAllTick = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeAllTick',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=entity__pb2.ErrorMessage.FromString,
                )
        self.UnSubscribeAllBidAsk = channel.unary_unary(
                '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeAllBidAsk',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=entity__pb2.ErrorMessage.FromString,
                )


class SubscribeDataInterfaceServicer(object):
    """SubscribeDataInterface is the interface for subscribe data
    """

    def SubscribeStockTick(self, request, context):
        """SubscribeStockTick is the interface for subscribe stock tick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockTick(self, request, context):
        """UnSubscribeStockTick is the interface for unsubscribe stock tick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeStockBidAsk(self, request, context):
        """SubscribeStockBidAsk is the interface for subscribe stock bid ask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockBidAsk(self, request, context):
        """UnSubscribeStockBidAsk is the interface for unsubscribe stock bid ask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeFutureTick(self, request, context):
        """SubscribeFutureTick is the interface for subscribe stock all tick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeFutureTick(self, request, context):
        """UnSubscribeFutureTick is the interface for unsubscribe stock all tick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeFutureBidAsk(self, request, context):
        """SubscribeFutureBidAsk is the interface for subscribe stock all bid ask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeFutureBidAsk(self, request, context):
        """UnSubscribeFutureBidAsk is the interface for unsubscribe stock all bid ask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeAllTick(self, request, context):
        """UnSubscribeAllTick is the interface for unsubscribe stock all tick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeAllBidAsk(self, request, context):
        """UnSubscribeStockAllBidAsk is the interface for unsubscribe stock all bid ask
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubscribeDataInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeStockTick': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeStockTick,
                    request_deserializer=entity__pb2.StockNumArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockTick,
                    request_deserializer=entity__pb2.StockNumArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeStockBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeStockBidAsk,
                    request_deserializer=entity__pb2.StockNumArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockBidAsk,
                    request_deserializer=entity__pb2.StockNumArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeFutureTick': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeFutureTick,
                    request_deserializer=entity__pb2.FutureCodeArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeFutureTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeFutureTick,
                    request_deserializer=entity__pb2.FutureCodeArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeFutureBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeFutureBidAsk,
                    request_deserializer=entity__pb2.FutureCodeArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeFutureBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeFutureBidAsk,
                    request_deserializer=entity__pb2.FutureCodeArr.FromString,
                    response_serializer=subscribe__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeAllTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeAllTick,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=entity__pb2.ErrorMessage.SerializeToString,
            ),
            'UnSubscribeAllBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeAllBidAsk,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=entity__pb2.ErrorMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'toc_python_forwarder.SubscribeDataInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubscribeDataInterface(object):
    """SubscribeDataInterface is the interface for subscribe data
    """

    @staticmethod
    def SubscribeStockTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/SubscribeStockTick',
            entity__pb2.StockNumArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeStockTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeStockTick',
            entity__pb2.StockNumArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeStockBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/SubscribeStockBidAsk',
            entity__pb2.StockNumArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeStockBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeStockBidAsk',
            entity__pb2.StockNumArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeFutureTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/SubscribeFutureTick',
            entity__pb2.FutureCodeArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeFutureTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeFutureTick',
            entity__pb2.FutureCodeArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeFutureBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/SubscribeFutureBidAsk',
            entity__pb2.FutureCodeArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeFutureBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeFutureBidAsk',
            entity__pb2.FutureCodeArr.SerializeToString,
            subscribe__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeAllTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeAllTick',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            entity__pb2.ErrorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeAllBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.SubscribeDataInterface/UnSubscribeAllBidAsk',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            entity__pb2.ErrorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
