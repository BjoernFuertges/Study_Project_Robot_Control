"""The Python implementation of the GRPC webcontroller.Agent server."""

from concurrent import futures
import logging

import grpc
from protos_generated import webcontroller_pb2
from protos_generated import webcontroller_pb2_grpc

from webcontroller import status_management

class Agent(webcontroller_pb2_grpc.AgentServicer):
    sm = status_management.status_manager("IRobot")

    def MoveInformation(self, request, context):
        return self.Sm_To_mir()
    
    def MoveInformationGetLastSended(self, request, context):
        return self.Sm_To_mirws()
    
    def MoveInformationGetNew(self, request, context):
        self.sm.passed_to_robot = True
        return self.Sm_To_mir()
    
    def MoveInformationHasNew(self, request, context):
        return webcontroller_pb2.MoveInformationHasNewReply(
            hasNew=(self.sm.passed_to_robot == False)
        )

    def MoveInformationDeliveryLeft (self, request, context):
        self.sm.set_turn_speed_radius('left', request.speed, request.radius)
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryRight (self, request, context):
        self.sm.set_turn_speed_radius('right', request.speed, request.radius)
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryCenter (self, request, context):
        self.sm.set_turn_speed_radius('no', request.speed, request.radius)
        return self.Sm_To_mir()

    def MoveInformationDeliveryForward (self, request, context):
        self.sm.set_direction_speed_radius('forward', request.speed, request.radius)
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryBackward (self, request, context):
        self.sm.set_direction_speed_radius('backward', request.speed, request.radius)
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryChangeLeft (self, request, context):
        self.sm.turn = 'left'
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryChangeRight (self, request, context):
        self.sm.turn = 'right'
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryChangeCenter (self, request, context):
        self.sm.turn = 'no'
        return self.Sm_To_mir()

    def MoveInformationDeliveryChangeForward (self, request, context):
        logging.debug("Called MoveInformationDeliveryChangeForward")
        print("Called MoveInformationDeliveryChangeForward")
        self.sm.direction = 'forward'
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryChangeBackward (self, request, context):
        self.sm.direction = 'backward'
        return self.Sm_To_mir()
    
    def MoveInformationDeliveryStop (self, request, context):
        self.sm.stop = request.stop
        print("MoveInformationDeliveryStop")
        return self.Sm_To_mir()
    
    def Sm_To_mir(self) -> webcontroller_pb2.MoveInformationReply:
        return webcontroller_pb2.MoveInformationReply(
            name = self.sm.name, 
            stop = self.sm.stop,
            speed = self.sm.speed,
            direction = self.sm.direction,
            turn = self.sm.turn,
            radius = self.sm.radius
        )
    
    def Sm_To_mirws(self) -> webcontroller_pb2.MoveInformationReplyWithStatus:
        return webcontroller_pb2.MoveInformationReplyWithStatus(
            name = self.sm.name, 
            stop = self.sm.stop,
            speed = self.sm.speed,
            direction = self.sm.direction,
            turn = self.sm.turn,
            radius = self.sm.radius,
            passedToRobot = self.sm.passed_to_robot
        )

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