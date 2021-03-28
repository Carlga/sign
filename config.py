import json,os

from jingyi import Jingyisign
from jingdong import Jingdong
from weather import Weather
from yingdi import Yingdi

checkin_map = {
    "JYLT_LIST":("精易论坛",Jingyisign),
    "JD_LIST":("京东签到",Jingdong),
    "CITY_NAME_LIST": ("天气预报", Weather),
    "WZYD_LIST":("王者营地",Yingdi)
}

notice_map={
    "QMSG_KEY": "",
    "QYWX_CORPID": "",
    "QYWX_CORPSECRET": "",
    "QYWX_AGENTID": "",
}



def get_checkin_info(data):
    result = {}
    if isinstance(data, dict):
        for one in checkin_map.keys():
            result[one.lower()] = data.get(one,[])

    return result


def get_notice_info(data):
    result = {}
    if isinstance(data, dict):
        for one in notice_map.keys():
            result[one.lower()] = data.get(one, None)

    return result
