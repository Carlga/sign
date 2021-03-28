# -*- coding: utf8 -*-
import requests,json

qywx_token = ''

def msg_qmsg(qmsg_key,content):
    print('qmsg酱推送')
    r = requests.get(f'https://qmsg.zendee.cn:443/send/{qmsg_key}?msg={content}')
    return r.text


def msg_qywxapp(qywx_corpid,qywx_corpsecret,qywx_agentid,content):
    global qywx_token
    print('企业微信应用推送')
    if not qywx_token:
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={qywx_corpid}&corpsecret={qywx_corpsecret}')
        qywx_token = res.json().get('access_token','')

    data = {
        'touser':'@all',
        'msgtype':'textcard',
        'agentid':qywx_agentid,
        'textcard':{
            'title': '签到通知',
            'description': content,
            'url': 'https://github.com/Carlga/sign'
        }
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={qywx_token}',json=data)
    # print(r.text)
    return r.text

def push_msg(content_list:list,notice_info: dict):


    qmsg_key=notice_info.get('qmsg_key')
    qywx_corpid=notice_info.get('qywx_corpid')
    qywx_corpsecret=notice_info.get('qywx_corpsecret')
    qywx_agentid=notice_info.get('qywx_agentid')

    for content in content_list:
        if qmsg_key:
            try:
                msg_qmsg(qmsg_key=qmsg_key,content=content)
            except Exception as e:
                print('qsmg酱推送失败',e)

        if qywx_corpid and qywx_corpsecret and qywx_agentid:
            try:
                msg_qywxapp(qywx_corpid,qywx_corpsecret,qywx_agentid,content)
            except Exception as e:
                print('企业微信应用推送失败',e)





