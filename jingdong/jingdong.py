# -*- coding: utf8 -*-
import requests,time


def strTodict_data(str,):
    return {i.split('=')[0]: i.split('=')[1] for i in str.split('&')}

class Jingdong():
    def __init__(self,check_item):
        self.check_item = check_item

    @staticmethod
    def jdjr_sign(cookie):
        msg = '京东金融：\t'
        url = f'https://ms.jr.jd.com/gw/generic/hy/h5/m/signIn1?_={str(int(time.time() * 1000))}'
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Cookie': cookie
        }

        data = strTodict_data(
            r'reqData={"videoId":"311372930347370496","channelSource":"JRAPP6.0","channelLv":"icon","riskDeviceParam":"{\"deviceType\":\"ASUS_I001DA\",\"traceIp\":\"\",\"macAddress\":\"04D9F5B66AE2\",\"imei\":\"7e1bc653071a3bcd\",\"os\":\"android\",\"osVersion\":\"10\",\"fp\":\"7310aaff3cd6f2d71d04ca34c95a40dd\",\"ip\":\"192.168.52.130\",\"eid\":\"\",\"appId\":\"com.jd.jrapp\",\"openUUID\":\"\",\"uuid\":\"7e1bc653071a3bcd-04D9F5B66AE2\",\"clientVersion\":\"6.1.10\",\"resolution\":\"1080.0*2304.0\",\"channelInfo\":\"tencent#50966\",\"networkType\":\"wifi\",\"startNo\":\"215\",\"openid\":\"\",\"token\":\"\",\"sid\":\"\",\"terminalType\":\"02\",\"longtitude\":\"\",\"latitude\":\"\",\"securityData\":\"\",\"jscContent\":\"\",\"fnHttpHead\":\"\",\"receiveRequestTime\":\"\",\"port\":\"\",\"appType\":3,\"optType\":\"\",\"idfv\":\"\",\"wifiSSID\":\"\",\"wifiMacAddress\":\"\",\"cellIpAddress\":\"\",\"wifiIpAddress\":\"\",\"sdkToken\":\"ZKSLQ7IJZYAO5ECBMVOLV2BIYR3UP7MZZO54MC4VHI6L4LVJK7NQMYJEYR3A5NCY2ZS4VTRZH44LI\"}"}')
        r = requests.post(url, data=data, headers=headers)
        # print(r.text)

        try:
            if r.json().get('resultCode') == 0:
                msg = msg + r.json()['resultData']['resBusiMsg']
            else:
                msg = msg + r.json()['resultMsg']
        except:
            msg = msg + '接口异常'
        return msg

    @staticmethod
    def jd_sign(cookie):
        msg = '京东：    \t'
        url = 'https://api.m.jd.com/client.action'
        headers = {
            'User-Agent': 'okhttp/3.12.1',
            'Cookie': cookie
        }
        params = strTodict_data(
            'functionId=signBeanAct&clientVersion=9.4.2&client=android&uuid=ffe63cbc15cb26e5&st=1615788848580&sign=9d274ce046fd9b96654d1609dc7a6326&sv=120')
        data = strTodict_data(
            'body={"eid":"eidA29a781231ds7pXKo8GogStaBrklx1T5AJqVyqmICeLMmGIcrPdjrFsSYepjIDeW1ZDRYe7iyUVSILQZlNBJ3nROm31PubyzIZEVL2+qWUMc3Uylj","fp":"-1","jda":"-1","referUrl":"-1","rnVersion":"4.7","shshshfp":"-1","shshshfpa":"-1","userAgent":"-1"}')
        r = requests.post(url, params=params, data=data, headers=headers)
        # print(r.text)
        try:
            if r.json().get('code') == '0':
                if r.json().get('data').get('dailyAward') != None:
                    msg = msg + r.json()['data']['dailyAward']['title'] + r.json()['data']['dailyAward']['subTitle'] + \
                          r.json()['data']['dailyAward']['beanAward']['beanCount'] + '金豆'
                else:
                    # msg = msg + r.json()['errorMessage']
                    msg += r.json()['data']['continuityAward']['title'] + 'X' + \
                           r.json()['data']['continuityAward']['beanAward']['beanCount'] + '金豆'
            else:
                # msg += r.json()['data']['continuityAward']['title'] + 'X' + r.json()['data']['continuityAward']['beanAward']['beanCount'] + '金豆'
                msg = msg + r.json()['errorMessage']
        except:
            msg = msg + '接口异常'
        return msg

    @staticmethod
    def jdsq_sign(cookie):
        msg = '京东双签：\t'
        url = f'https://nu.jr.jd.com/gw/generic/jrm/h5/m/process?_={str(int(time.time() * 1000))}'
        headers = {
            'User-Agent': 'jdapp;android;9.4.2',
            'Cookie': cookie
        }
        data = strTodict_data(
            r'reqData={"actCode":"F68B2C3E71","type":4,"frontParam":{"belong":"jingdou"},"riskDeviceParam":"{\"fp\":\"6dde9fd5304637fbfc02732f13f557b4\",\"eid\":\"JBHIUJCYEGZBSQLXTERPGPYMU2NDTH2WKPDZKDZJYGMMPXM4KX4NBKFYGSXXFSPKPTL52WMW6ZQ6CP7SMMY4ZKZUAE\",\"sdkToken\":\"\",\"sid\":\"\"}"}')
        r = requests.post(url, data=data, headers=headers)
        # print(r.text)
        try:
            if r.json().get('resultCode') == 0:
                try:
                    msg = msg + '成功领取' + \
                          r.json()['resultData']['data']['businessData']['businessData']['awardListVo'][0]['name']
                except:
                    msg = msg + r.json()['resultData']['data']['businessData']['businessMsg']
            else:
                msg = msg + r.json()['resultMsg']
        except:
            msg = msg + '接口异常'
        return msg

    def main(self):
        jd_cookie = self.check_item.get('jd_cookie')
        jd_msg = self.jd_sign(jd_cookie)
        jdjr_msg = self.jdjr_sign(jd_cookie)
        jdsq_msg = self.jdsq_sign(jd_cookie)
        msg = jd_msg + '\n' + jdjr_msg + '\n' + jdsq_msg

        return msg