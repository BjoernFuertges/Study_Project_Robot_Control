from __future__ import print_function

import logging

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = webcontroller_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(webcontroller_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

def start():
    logging.basicConfig()
    run()


if __name__ == '__main__':
    logging.basicConfig()
    run()