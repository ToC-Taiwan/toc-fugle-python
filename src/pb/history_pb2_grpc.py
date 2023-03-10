# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import history_pb2 as history__pb2


class HistoryDataInterfaceStub(object):
    """HistoryDataInterface is the interface for history data
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStockHistoryTick = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryTick',
                request_serializer=history__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=history__pb2.HistoryTickResponse.FromString,
                )
        self.GetStockHistoryKbar = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryKbar',
                request_serializer=history__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=history__pb2.HistoryKbarResponse.FromString,
                )
        self.GetStockHistoryClose = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryClose',
                request_serializer=history__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=history__pb2.HistoryCloseResponse.FromString,
                )
        self.GetStockHistoryCloseByDateArr = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryCloseByDateArr',
                request_serializer=history__pb2.StockNumArrWithDateArr.SerializeToString,
                response_deserializer=history__pb2.HistoryCloseResponse.FromString,
                )
        self.GetFutureHistoryTick = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetFutureHistoryTick',
                request_serializer=history__pb2.FutureCodeArrWithDate.SerializeToString,
                response_deserializer=history__pb2.HistoryTickResponse.FromString,
                )
        self.GetFutureHistoryKbar = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetFutureHistoryKbar',
                request_serializer=history__pb2.FutureCodeArrWithDate.SerializeToString,
                response_deserializer=history__pb2.HistoryKbarResponse.FromString,
                )
        self.GetFutureHistoryClose = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetFutureHistoryClose',
                request_serializer=history__pb2.FutureCodeArrWithDate.SerializeToString,
                response_deserializer=history__pb2.HistoryCloseResponse.FromString,
                )
        self.GetStockTSEHistoryTick = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockTSEHistoryTick',
                request_serializer=history__pb2.Date.SerializeToString,
                response_deserializer=history__pb2.HistoryTickResponse.FromString,
                )
        self.GetStockTSEHistoryKbar = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockTSEHistoryKbar',
                request_serializer=history__pb2.Date.SerializeToString,
                response_deserializer=history__pb2.HistoryKbarResponse.FromString,
                )
        self.GetStockTSEHistoryClose = channel.unary_unary(
                '/toc_python_forwarder.HistoryDataInterface/GetStockTSEHistoryClose',
                request_serializer=history__pb2.Date.SerializeToString,
                response_deserializer=history__pb2.HistoryCloseResponse.FromString,
                )


class HistoryDataInterfaceServicer(object):
    """HistoryDataInterface is the interface for history data
    """

    def GetStockHistoryTick(self, request, context):
        """GetStockHistoryTick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryKbar(self, request, context):
        """GetStockHistoryKbar
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryClose(self, request, context):
        """GetStockHistoryClose
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryCloseByDateArr(self, request, context):
        """GetStockHistoryCloseByDateArr
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFutureHistoryTick(self, request, context):
        """GetFutureHistoryTick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFutureHistoryKbar(self, request, context):
        """GetFutureHistoryKbar
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFutureHistoryClose(self, request, context):
        """GetFutureHistoryClose
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockTSEHistoryTick(self, request, context):
        """GetStockTSEHistoryTick
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockTSEHistoryKbar(self, request, context):
        """GetStockTSEHistoryKbar
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockTSEHistoryClose(self, request, context):
        """GetStockTSEHistoryClose
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HistoryDataInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStockHistoryTick': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryTick,
                    request_deserializer=history__pb2.StockNumArrWithDate.FromString,
                    response_serializer=history__pb2.HistoryTickResponse.SerializeToString,
            ),
            'GetStockHistoryKbar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryKbar,
                    request_deserializer=history__pb2.StockNumArrWithDate.FromString,
                    response_serializer=history__pb2.HistoryKbarResponse.SerializeToString,
            ),
            'GetStockHistoryClose': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryClose,
                    request_deserializer=history__pb2.StockNumArrWithDate.FromString,
                    response_serializer=history__pb2.HistoryCloseResponse.SerializeToString,
            ),
            'GetStockHistoryCloseByDateArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryCloseByDateArr,
                    request_deserializer=history__pb2.StockNumArrWithDateArr.FromString,
                    response_serializer=history__pb2.HistoryCloseResponse.SerializeToString,
            ),
            'GetFutureHistoryTick': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFutureHistoryTick,
                    request_deserializer=history__pb2.FutureCodeArrWithDate.FromString,
                    response_serializer=history__pb2.HistoryTickResponse.SerializeToString,
            ),
            'GetFutureHistoryKbar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFutureHistoryKbar,
                    request_deserializer=history__pb2.FutureCodeArrWithDate.FromString,
                    response_serializer=history__pb2.HistoryKbarResponse.SerializeToString,
            ),
            'GetFutureHistoryClose': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFutureHistoryClose,
                    request_deserializer=history__pb2.FutureCodeArrWithDate.FromString,
                    response_serializer=history__pb2.HistoryCloseResponse.SerializeToString,
            ),
            'GetStockTSEHistoryTick': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockTSEHistoryTick,
                    request_deserializer=history__pb2.Date.FromString,
                    response_serializer=history__pb2.HistoryTickResponse.SerializeToString,
            ),
            'GetStockTSEHistoryKbar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockTSEHistoryKbar,
                    request_deserializer=history__pb2.Date.FromString,
                    response_serializer=history__pb2.HistoryKbarResponse.SerializeToString,
            ),
            'GetStockTSEHistoryClose': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockTSEHistoryClose,
                    request_deserializer=history__pb2.Date.FromString,
                    response_serializer=history__pb2.HistoryCloseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'toc_python_forwarder.HistoryDataInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HistoryDataInterface(object):
    """HistoryDataInterface is the interface for history data
    """

    @staticmethod
    def GetStockHistoryTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryTick',
            history__pb2.StockNumArrWithDate.SerializeToString,
            history__pb2.HistoryTickResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryKbar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryKbar',
            history__pb2.StockNumArrWithDate.SerializeToString,
            history__pb2.HistoryKbarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryClose',
            history__pb2.StockNumArrWithDate.SerializeToString,
            history__pb2.HistoryCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryCloseByDateArr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockHistoryCloseByDateArr',
            history__pb2.StockNumArrWithDateArr.SerializeToString,
            history__pb2.HistoryCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFutureHistoryTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetFutureHistoryTick',
            history__pb2.FutureCodeArrWithDate.SerializeToString,
            history__pb2.HistoryTickResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFutureHistoryKbar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetFutureHistoryKbar',
            history__pb2.FutureCodeArrWithDate.SerializeToString,
            history__pb2.HistoryKbarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFutureHistoryClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetFutureHistoryClose',
            history__pb2.FutureCodeArrWithDate.SerializeToString,
            history__pb2.HistoryCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockTSEHistoryTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockTSEHistoryTick',
            history__pb2.Date.SerializeToString,
            history__pb2.HistoryTickResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockTSEHistoryKbar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockTSEHistoryKbar',
            history__pb2.Date.SerializeToString,
            history__pb2.HistoryKbarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockTSEHistoryClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/toc_python_forwarder.HistoryDataInterface/GetStockTSEHistoryClose',
            history__pb2.Date.SerializeToString,
            history__pb2.HistoryCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
