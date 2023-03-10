# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import simple_grpc_pb2 as simple__grpc__pb2


class SimpleGrpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/simplegrpc.SimpleGrpc/SayHello',
                request_serializer=simple__grpc__pb2.HelloReq.SerializeToString,
                response_deserializer=simple__grpc__pb2.HelloRes.FromString,
                )
        self.SayHelloToMany = channel.stream_unary(
                '/simplegrpc.SimpleGrpc/SayHelloToMany',
                request_serializer=simple__grpc__pb2.HelloReq.SerializeToString,
                response_deserializer=simple__grpc__pb2.HelloRes.FromString,
                )
        self.CheckInbox = channel.unary_stream(
                '/simplegrpc.SimpleGrpc/CheckInbox',
                request_serializer=simple__grpc__pb2.HelloReq.SerializeToString,
                response_deserializer=simple__grpc__pb2.HelloRes.FromString,
                )


class SimpleGrpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloToMany(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckInbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleGrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=simple__grpc__pb2.HelloReq.FromString,
                    response_serializer=simple__grpc__pb2.HelloRes.SerializeToString,
            ),
            'SayHelloToMany': grpc.stream_unary_rpc_method_handler(
                    servicer.SayHelloToMany,
                    request_deserializer=simple__grpc__pb2.HelloReq.FromString,
                    response_serializer=simple__grpc__pb2.HelloRes.SerializeToString,
            ),
            'CheckInbox': grpc.unary_stream_rpc_method_handler(
                    servicer.CheckInbox,
                    request_deserializer=simple__grpc__pb2.HelloReq.FromString,
                    response_serializer=simple__grpc__pb2.HelloRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'simplegrpc.SimpleGrpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleGrpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simplegrpc.SimpleGrpc/SayHello',
            simple__grpc__pb2.HelloReq.SerializeToString,
            simple__grpc__pb2.HelloRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloToMany(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/simplegrpc.SimpleGrpc/SayHelloToMany',
            simple__grpc__pb2.HelloReq.SerializeToString,
            simple__grpc__pb2.HelloRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckInbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/simplegrpc.SimpleGrpc/CheckInbox',
            simple__grpc__pb2.HelloReq.SerializeToString,
            simple__grpc__pb2.HelloRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
