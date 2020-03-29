# -*- coding: utf-8 -*-
import grpc

from proto import algo_pb2_grpc, algo_pb2


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = algo_pb2_grpc.AlgoServiceStub(channel)
    response = stub.getMultiModalData(algo_pb2.MultiModalRequest(type='multi', multiParamter='multiParamter'))
    print("Greeter client received: " + response.data)
    response = stub.getSingleModalData(algo_pb2.SingleModalRequest(type='multi', singleParamter='singleParamter'))
    print("Greeter client received: " + response.data)

if __name__ == '__main__':
    run()