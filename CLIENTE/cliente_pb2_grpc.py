# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import cliente_pb2 as cliente__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in cliente_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MyUberServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterUser = channel.unary_unary(
                '/MyUberService/RegisterUser',
                request_serializer=cliente__pb2.UserRequest.SerializeToString,
                response_deserializer=cliente__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.GetServiceTypes = channel.unary_unary(
                '/MyUberService/GetServiceTypes',
                request_serializer=cliente__pb2.Empty.SerializeToString,
                response_deserializer=cliente__pb2.ServiceList.FromString,
                _registered_method=True)
        self.RequestTaxi = channel.unary_unary(
                '/MyUberService/RequestTaxi',
                request_serializer=cliente__pb2.TaxiRequest.SerializeToString,
                response_deserializer=cliente__pb2.TaxiResponse.FromString,
                _registered_method=True)


class MyUberServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestTaxi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyUberServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterUser,
                    request_deserializer=cliente__pb2.UserRequest.FromString,
                    response_serializer=cliente__pb2.RegisterResponse.SerializeToString,
            ),
            'GetServiceTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceTypes,
                    request_deserializer=cliente__pb2.Empty.FromString,
                    response_serializer=cliente__pb2.ServiceList.SerializeToString,
            ),
            'RequestTaxi': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestTaxi,
                    request_deserializer=cliente__pb2.TaxiRequest.FromString,
                    response_serializer=cliente__pb2.TaxiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MyUberService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('MyUberService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MyUberService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MyUberService/RegisterUser',
            cliente__pb2.UserRequest.SerializeToString,
            cliente__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetServiceTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MyUberService/GetServiceTypes',
            cliente__pb2.Empty.SerializeToString,
            cliente__pb2.ServiceList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestTaxi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MyUberService/RequestTaxi',
            cliente__pb2.TaxiRequest.SerializeToString,
            cliente__pb2.TaxiResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
