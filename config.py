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


def env2config(save_file=False):
    result = json.loads(os.getenv("CONFIG_JSON", {}).strip()) if os.getenv("CONFIG_JSON") else {}
    for one in checkin_map.keys():
        if one not in result.keys():
            result[one] = []
        check_items = env2list(one)
        result[one] += check_items
    for one in notice_map.keys():
        if not result.get(one):
            if env2str(one):
                result[one] = env2str(one)
    if not result.get("MOTTO"):
        result["MOTTO"] = os.getenv("MOTTO")
    if save_file:
        with open(os.path.join(os.path.dirname(__file__), "config/config.json"), "w+") as f:
            f.write(json.dumps(result))
    return result


def env2str(key):
    try:
        value = os.getenv(key, "") if os.getenv(key) else ""
        if isinstance(value, str):
            value = value.strip()
        elif isinstance(value, bool):
            value = value
        else:
            value = None
    except Exception as e:
        print(e)
        value = None
    return value


def get_checkin_info(data):
    result = {}
    if isinstance(data, dict):
        for one in checkin_map.keys():
            result[one.lower()] = data.get(one, [])
    else:
        for one in checkin_map.keys():
            result[one.lower()] = env2list(one)
    return result



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
