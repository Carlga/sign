# -*- coding: utf8 -*-
import requests,json



class Jingyisign():
    def __init__(self,check_item):
        self.check_item = check_item

    @staticmethod
    def sign(headers):
        session = requests.session()
        session.get(url='https://bbs.125.la/plugin.php?id=dsu_paulsign:sign',headers=headers)
        data = {
            'formhash':'e341b2ce',
            'submit':'1',
            'targerurl':'',
            'todaysay':'',
            'qdxq':'wl'

        }
        r = session.post(url='https://bbs.125.la/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1',headers=headers,data=data)
        # print(r.text)
        try:
            if r.json()['status'] == 1:
                msg = '精易论坛签到成功'
            else:
                msg = '精易论坛签到失败 \n'
                msg += r.json()['msg']
        except Exception as e:
            print('精易论坛签到错误，原因:',e)
            msg = '精易论坛签到错误'
        return msg

    def main(self):
        jylt_cookie = self.check_item.get('jylt_cookie')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57',
            'Cookie':jylt_cookie
        }
        msg = self.sign(headers)


        return msg

