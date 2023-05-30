"""The Python implementation of the GRPC webcontroller.Agent server."""

from concurrent import futures
import logging

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

import status_management

class Agent(webcontroller_pb2_grpc.AgentServicer):
    sm = status_management.status_manager()

    def MoveInformation(self, request, context):
        return webcontroller_pb2.MoveInformationReply(name='Hello, %s!' % request.name, stop=False, speed=100, direction="forward", turn="no", radius=0.8)
    
    def MoveInformationDeliveryLeft (self, request, context):
        return webcontroller_pb2.MoveInformationReply(name='Hello, %s!' % request.name, stop=False, speed=100, direction="forward", turn="no", radius=0.8)
    
    def MoveInformationDeliveryRight (self, request, context):
        return webcontroller_pb2.MoveInformationReply(name='Hello, %s!' % request.name, stop=False, speed=100, direction="forward", turn="no", radius=0.8)
    
    def MoveInformationDeliveryForward (self, request, context):
        return webcontroller_pb2.MoveInformationReply(name='Hello, %s!' % request.name, stop=False, speed=100, direction="forward", turn="no", radius=0.8)
    
    def MoveInformationDeliveryBackward (self, request, context):
        return webcontroller_pb2.MoveInformationReply(name='Hello, %s!' % request.name, stop=False, speed=100, direction="forward", turn="no", radius=0.8)
    
    def MoveInformationDeliveryStop (self, request, context):
        return webcontroller_pb2.MoveInformationReply(name='Hello, %s!' % request.name, stop=False, speed=100, direction="forward", turn="no", radius=0.8)
    
def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    webcontroller_pb2_grpc.add_AgentServicer_to_server(Agent(), server)
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