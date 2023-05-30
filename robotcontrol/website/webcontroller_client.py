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
        stub = webcontroller_pb2_grpc.AgentStub(channel)
        response = stub.MoveInformation(webcontroller_pb2.MoveInformationRequest(name='you'))
    print("Agent client received: " + response.name + ", " + str(response.stop) + ", " + str(response.speed) + ", " + response.direction + ", " + response.turn + ", " + str(response.radius))

def start():
    logging.basicConfig()
    run()


if __name__ == '__main__':
    logging.basicConfig()
    run()