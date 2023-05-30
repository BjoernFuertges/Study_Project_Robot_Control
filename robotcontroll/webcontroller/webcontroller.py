"""The Python implementation of the GRPC webcontroller.Greeter server."""

from concurrent import futures
import logging

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

class Greeter(webcontroller_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return webcontroller_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    webcontroller_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

def start():
    logging.basicConfig()
    serve()

if __name__ == '__main__':
    logging.basicConfig()
    serve()