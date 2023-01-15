# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import trade_pb2 as trade__pb2


class TradeInterfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BuyStock = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/BuyStock',
                request_serializer=trade__pb2.StockOrderDetail.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.SellStock = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/SellStock',
                request_serializer=trade__pb2.StockOrderDetail.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.SellFirstStock = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/SellFirstStock',
                request_serializer=trade__pb2.StockOrderDetail.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.CancelStock = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/CancelStock',
                request_serializer=trade__pb2.OrderID.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.GetLocalOrderStatusArr = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/GetLocalOrderStatusArr',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetSimulateOrderStatusArr = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/GetSimulateOrderStatusArr',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetOrderStatusByID = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/GetOrderStatusByID',
                request_serializer=trade__pb2.OrderID.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.GetNonBlockOrderStatusArr = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/GetNonBlockOrderStatusArr',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=common__pb2.ErrorMessage.FromString,
                )
        self.BuyFuture = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/BuyFuture',
                request_serializer=trade__pb2.FutureOrderDetail.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.SellFuture = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/SellFuture',
                request_serializer=trade__pb2.FutureOrderDetail.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.SellFirstFuture = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/SellFirstFuture',
                request_serializer=trade__pb2.FutureOrderDetail.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.CancelFuture = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/CancelFuture',
                request_serializer=trade__pb2.FutureOrderID.SerializeToString,
                response_deserializer=trade__pb2.TradeResult.FromString,
                )
        self.GetFuturePosition = channel.unary_unary(
                '/sinopac_forwarder.TradeInterface/GetFuturePosition',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=trade__pb2.FuturePositionArr.FromString,
                )


class TradeInterfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BuyStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellFirstStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLocalOrderStatusArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimulateOrderStatusArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderStatusByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNonBlockOrderStatusArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuyFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellFirstFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFuturePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TradeInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BuyStock': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyStock,
                    request_deserializer=trade__pb2.StockOrderDetail.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'SellStock': grpc.unary_unary_rpc_method_handler(
                    servicer.SellStock,
                    request_deserializer=trade__pb2.StockOrderDetail.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'SellFirstStock': grpc.unary_unary_rpc_method_handler(
                    servicer.SellFirstStock,
                    request_deserializer=trade__pb2.StockOrderDetail.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'CancelStock': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelStock,
                    request_deserializer=trade__pb2.OrderID.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'GetLocalOrderStatusArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocalOrderStatusArr,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetSimulateOrderStatusArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimulateOrderStatusArr,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetOrderStatusByID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderStatusByID,
                    request_deserializer=trade__pb2.OrderID.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'GetNonBlockOrderStatusArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNonBlockOrderStatusArr,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=common__pb2.ErrorMessage.SerializeToString,
            ),
            'BuyFuture': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyFuture,
                    request_deserializer=trade__pb2.FutureOrderDetail.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'SellFuture': grpc.unary_unary_rpc_method_handler(
                    servicer.SellFuture,
                    request_deserializer=trade__pb2.FutureOrderDetail.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'SellFirstFuture': grpc.unary_unary_rpc_method_handler(
                    servicer.SellFirstFuture,
                    request_deserializer=trade__pb2.FutureOrderDetail.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'CancelFuture': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelFuture,
                    request_deserializer=trade__pb2.FutureOrderID.FromString,
                    response_serializer=trade__pb2.TradeResult.SerializeToString,
            ),
            'GetFuturePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFuturePosition,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=trade__pb2.FuturePositionArr.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sinopac_forwarder.TradeInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TradeInterface(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BuyStock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/BuyStock',
            trade__pb2.StockOrderDetail.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellStock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/SellStock',
            trade__pb2.StockOrderDetail.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellFirstStock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/SellFirstStock',
            trade__pb2.StockOrderDetail.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelStock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/CancelStock',
            trade__pb2.OrderID.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLocalOrderStatusArr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/GetLocalOrderStatusArr',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSimulateOrderStatusArr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/GetSimulateOrderStatusArr',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrderStatusByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/GetOrderStatusByID',
            trade__pb2.OrderID.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNonBlockOrderStatusArr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/GetNonBlockOrderStatusArr',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            common__pb2.ErrorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuyFuture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/BuyFuture',
            trade__pb2.FutureOrderDetail.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellFuture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/SellFuture',
            trade__pb2.FutureOrderDetail.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellFirstFuture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/SellFirstFuture',
            trade__pb2.FutureOrderDetail.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelFuture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/CancelFuture',
            trade__pb2.FutureOrderID.SerializeToString,
            trade__pb2.TradeResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFuturePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.TradeInterface/GetFuturePosition',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            trade__pb2.FuturePositionArr.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
