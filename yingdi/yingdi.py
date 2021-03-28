import requests,time
from random import randint

def strTodict_data(str:str):
    return {i.split('=')[0]: i.split('=')[1] for i in str.split('&')}

headers = {
            'User-Agent': 'okhttp/3.12.12',
            'gameAreaId': '1',
            'gameId': '20001',
            'gameOpenId': '',
            'gameRoleId': '',
            'gameServerId': '',
            'gameUserSex': '0'

        }


class Yingdi():
    def __init__(self,check_item):
        self.check_item = check_item

    @staticmethod
    def start_user(dict):
        url = 'https://ssl.kohsocialapp.qq.com:10001/user/login'
        data_str = 'delOldUser=0&lastGetRemarkTime=0&lastLoginTime=&loginType=openSdk&token=&userId=&cChannelId=2002&cClientVersionCode=2021562108&cClientVersionName=5.62.108&cCurrentGameId=20001&cGameId=20001&cGzip=1&cRand=&cSystem=android&cSystemVersionCode=29&cSystemVersionName=10&gameAreaId=1&gameId=20001&gameOpenId=&gameRoleId=&gameServerId=&gameUserSex=1&tinkerId=2021562108_0'
        data = strTodict_data(data_str)
        data.update(dict)
        head = headers.copy()
        head.update(dict)
        data['lastLoginTime'] = str(int(time.time()))
        data['rRand'] = str(int(time.time() * 1000))
        r = requests.post(url, data=data, headers=head)
        # print(r.text)
        # print(r.request.headers)
        if r.json()['result'] == 0:
            msg = '刷新token成功'
        else:
            msg = '刷新token失败'
        return msg

    # 获取首页资讯
    def get_zixun(self,dict):
        url = 'https://ssl.kohsocialapp.qq.com:10001/info/listinfo'
        head = headers.copy()
        head.update(dict)
        data_str = 'type=25818&feedNum=0&filterVideo=0&oaid=&pos1=1&taid=0101869F97609C28A5E6A6E7CE6403672940D00E1B115CBDF07E45D16426F55724EEFAACC425FD39DCF15CCF&page=1&scenario=DEFAULT&cChannelId=2002&cClientVersionCode=2021562108&cClientVersionName=5.62.108&cCurrentGameId=20001&cGameId=20001&cGzip=1&cRand=1615253068274&cSystem=android&cSystemVersionCode=29&cSystemVersionName=10&gameAreaId=1&gameId=20001&gameOpenId=&gameRoleId=&gameServerId=&gameUserSex=1&tinkerId=2021562108_0&token=&userId='
        data = strTodict_data(data_str)
        data.update(dict)
        data['rRand'] = str(int(time.time() * 1000))
        r = requests.post(url, data=data, headers=head)
        # print(r.text)
        try:
            for i in range(1, 9):
                # print(r.text)
                iInfoId = r.json()['data']['list'][i]['iInfoId']
                algoType = r.json()['data']['list'][i]['algoType']
                docid = r.json()['data']['list'][i]['docid']
                tuple1 = (i, iInfoId, algoType)
                tuple2 = (iInfoId, docid)
                # print(tuple)
                msg_ll = self.get_liulan(dict, tuple1)
                msg_dz = self.get_dianzan(dict, tuple2)
            if '点赞成功' in msg_dz:
                msg = msg_ll + '-----' + msg_dz
            else:
                msg = msg_ll + '-----' + msg_dz
        except Exception as e:
            msg = f'任务失败，请检查接口,{e}'
            print(e)

        return msg

    # 浏览资讯
    @staticmethod
    def get_liulan(dict, tuple):
        pos, iInfoId, algoType = tuple
        url = 'https://ssl.kohsocialapp.qq.com:10001/game/detailinfov3'
        head = headers.copy()
        head.update(dict)
        data_str = 'algoType=984722&apiVersion=1&type=25818&pos1=1&friendReadNum=0&goPickComment=0&iInfoId=180508050&pos=2&pos2=0&targetCommentId=0&targetCommentTime=0&taskId=0&cChannelId=2002&cClientVersionCode=2021562108&cClientVersionName=5.62.108&cCurrentGameId=20001&cGameId=20001&cGzip=1&cRand=1615259458940&cSystem=android&cSystemVersionCode=29&cSystemVersionName=10&gameAreaId=1&gameId=20001&gameOpenId=&gameRoleId=&gameServerId=&gameUserSex=1&key1=de6f8a634a78e3e14ab38c85312cc69baa4aa4f0&key10=106692&key11=armeabi-v7a%24armeabi&key13=WIFI&key14=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&key2=de6f8a634a78e3e14ab38c85312cc69baa4aa4f0&key3=53949a23b94c6aac&key4=02%3A00%3A00%3A00%3A00%3A00&key5=356&key6=1080&key7=2340&key8=asus&key9=ASUS_I001DA&tinkerId=2021562108_0&token=&userId='
        data = strTodict_data(data_str)
        data.update(dict)
        data['pos'] = pos
        data['iInfoId'] = iInfoId
        data['algoType'] = algoType
        data['rRand'] = str(int(time.time() * 1000))
        r = requests.post(url, data=data, headers=head)
        try:
            if r.json()['result'] != 0:
                msg = '浏览失败,原因：' + r.json()['returnMsg']
            else:
                msg = '浏览成功'
        except Exception as e:
            msg = f'任务失败，请检查接口,{e}'
            print(e)
        return msg

    # 点赞
    @staticmethod
    def get_dianzan(dict, tuple):
        iInfoId, docid = tuple
        url = 'https://ssl.kohsocialapp.qq.com:10001/user/addlike'
        head = headers.copy()
        head.update(dict)
        data_str = 'iInfoId=&docid=&like=1&cChannelId=2002&cClientVersionCode=2021562108&cClientVersionName=5.62.108&cCurrentGameId=20001&cGameId=20001&cGzip=1&cRand=1615261501342&cSystem=android&cSystemVersionCode=29&cSystemVersionName=10&gameAreaId=1&gameId=20001&gameOpenId=&gameRoleId=&gameServerId=&gameUserSex=1&tinkerId=&token=&userId='
        data = strTodict_data(data_str)
        data.update(dict)
        data['rRand'] = str(int(time.time() * 1000))
        data['docid'] = docid
        data['iInfoId'] = iInfoId
        # print(data)
        r = requests.post(url, data=data, headers=head)
        # print(r.text)
        # if r.json()['data']['like'] == True:
        try:
            if r.json()['result'] != 0:
                msg = '点赞失败,原因：' + r.json()['returnMsg']
            else:
                msg = '点赞成功'
        except Exception as e:
            msg = f'任务失败，请检查接口,{e}'
            print(e)
        return msg

    # 领取浏览奖励
    @staticmethod
    def get_liulan_lq(dict):
        url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5taskgetgift'
        head = {
            'User-Agent': 'Mozilla/5.0'
        }
        data_str = 'appVersion=2021562108&serverId=&gameId=20001&roleId=&cClientVersionName=5.62.108&userId=&gameOpenid=&areaId=1&platid=1&algorithm=v2&appid=1105200115&encode=2&openid=&sig=&source=smoba_zhushou&timestamp=&version=3.1.96a&msdkEncodeParam=8FCF27AF0A75528A03267FDB309B87EEF056BB73A2DBFBF7AAF4B509032112246D67ED60263B8CC94D9CFEAAEA8267F2C2274DB8308B282DC85C8CF5EEAA039FC163D1333064F9DF82D1A840448B27782294BA726E774608D0F75BB1EBBE46DD9ED0489B46CBECEF8461DE4E35C0B0BEAEE468F49A945BA1A2D66B390213D75B4E94281086EBDD6FA8D31047FB58A1C0F162E107F92AA15A579834AB66187B890ADB324F9BD48B0EE2E7765399F9E92A&cSystem=android&h5Get=1&msdkToken=&taskId=2019071900007&giftType=&appOpenid='
        data = strTodict_data(data_str)
        data.update(dict)
        # data['timestamp'] = str(int(time.time() * 1000))
        data['taskId'] = '2019071900007'
        r = requests.post(url, data=data, headers=head)
        # print(r.text)
        try:
            if r.json()['result'] == 0:
                msg = '浏览奖励领取成功'
            else:
                msg = r.json()['returnMsg']
        except Exception as e:
            msg = f'请求失败,请检查接口,{e}'
        return msg

    # 领取点赞奖励
    @staticmethod
    def get_dianzan_lq(dict):
        url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5taskgetgift'
        head = {
            'User-Agent': 'Mozilla/5.0'
        }
        data_str = 'appVersion=2021562108&serverId=&gameId=20001&roleId=&cClientVersionName=5.62.108&userId=&gameOpenid=&areaId=1&platid=1&algorithm=v2&appid=1105200115&encode=2&openid=&sig=&source=smoba_zhushou&timestamp=&version=3.1.96a&msdkEncodeParam=8FCF27AF0A75528A03267FDB309B87EEF056BB73A2DBFBF7AAF4B509032112246D67ED60263B8CC94D9CFEAAEA8267F2C2274DB8308B282DC85C8CF5EEAA039FC163D1333064F9DF82D1A840448B27782294BA726E774608D0F75BB1EBBE46DD9ED0489B46CBECEF8461DE4E35C0B0BEAEE468F49A945BA1A2D66B390213D75B4E94281086EBDD6FA8D31047FB58A1C0F162E107F92AA15A579834AB66187B890ADB324F9BD48B0EE2E7765399F9E92A&cSystem=android&h5Get=1&msdkToken=&taskId=2019071900007&giftType=&appOpenid='
        data = strTodict_data(data_str)
        data.update(dict)
        # data['timestamp'] = str(int(time.time() * 1000))
        data['taskId'] = '2019071900008'
        r = requests.post(url, data=data, headers=head)
        # print(r.text)
        try:
            if r.json()['result'] == 0:
                msg = '点赞奖励领取成功'
            else:
                msg = r.json()['returnMsg']
        except Exception as e:
            msg = f'请求失败,请检查接口,{e}'
        return msg

    # 签到
    @staticmethod
    def qiandao(dict):
        url = 'https://ssl.kohsocialapp.qq.com:10001/play/h5sign'
        head = {
            'User-Agent': 'Mozilla/5.0'
        }
        data_str = 'appVersion=2021562108&serverId=&gameId=20001&roleId=&cClientVersionName=5.62.108&userId=&gameOpenid=&areaId=1&platid=1&algorithm=v2&appid=1105200115&encode=2&openid=&sig=&source=smoba_zhushou&timestamp=&version=3.1.96a&msdkEncodeParam=6AC25C7F1A9F9E967203EF10A1DF1AC4C6AF71E25761D8EAEE15D19260FDE9C2118440DC78E655E31FA7FA46F160A9D74A49D12EAE7AEBDF10F845A9BEC7D47053670256AD6F74B457CF2F5ADFBB3EC84C7409D4D5623E51CE766B8DBA93AD3DD886029141D102961017AF484DDF1FCCF88F41957689C3A48832551498A5F82764F4417AA78452F074F37602381D43CE243E25E2662F1A3F85D6FD2ACD3589D703952C33CABFAB863B8E71F5D06DF9B1&cSystem=android&h5Get=1&msdkToken=&appOpenid='
        data = strTodict_data(data_str)
        data.update(dict)
        # data['timestamp'] = str(int(time.time() * 1000))
        r = requests.post(url, data=data, headers=head)
        try:
            if r.json()['result'] == 0:
                msg = '签到成功'
            else:
                msg = r.json()['returnMsg']
        except Exception as e:
            msg = f'请求失败,请检查接口{e}'
        # print(data['serverId']+ ':  '+msg)
        return msg

    def main(self):
        user_set = self.check_item.get('user_set')
        user_sign = self.check_item.get('user_sign')
        today = int(time.strftime("%w"))

        msg_task = ''
        msg_task += self.start_user(user_set) + '\n'
        if today == 1:
            msg_task += self.get_zixun(user_set) + '\n'

        msg_sign = ''
        msg_sign += self.qiandao(user_sign) + '\n'
        if today == 1:
            msg_sign += self.get_liulan_lq(user_sign) + '\n'
            msg_sign += self.get_dianzan_lq(user_sign) + '\n'

        return msg_task + msg_sign
