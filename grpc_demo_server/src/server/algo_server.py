# -*- coding: utf-8 -*-
import grpc
from concurrent import futures
import logging

from src.proto import algo_pb2, algo_pb2_grpc
from src.server.algo_utils import algo_single_modal, algo_multi_modal


class Algo(algo_pb2_grpc.AlgoServiceServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def getSingleModalData(self, request, context):
        #to-do
        return algo_single_modal(request)

    def getMultiModalData(self, request, context):
        #to-do
        return algo_multi_modal(request)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    algo_pb2_grpc.add_AlgoServiceServicer_to_server(Algo(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()