# -*- coding: utf-8 -*-
#这个类中执行特定的算法
from proto.algo_pb2 import SingleModalResponse, MultiModalResponse


def algo_single_modal(singleModalRequest):
    return SingleModalResponse(type=singleModalRequest.type,data=singleModalRequest.singleParamter + " data response")

def algo_multi_modal(multiModalRequest):
    return MultiModalResponse(type=multiModalRequest.type,data=multiModalRequest.multiParamter + " data response")