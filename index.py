# -*- coding: utf8 -*-
import os,json
from config import checkin_map,get_checkin_info,get_notice_info, env2config
from msg.message import push_msg
from motto import Motto


def main():
    data = env2config()
    if data:        
        motto = data.get('MOTTO')
        check_info = get_checkin_info(data=data)
        notice_info = get_notice_info(data=data)
    content_list = []
    # print(check_info)
    for one_check,check_tuple in checkin_map.items():
        check_name, check_func = check_tuple
        if check_info.get(one_check.lower()):
            print(f"----------已检测到正确的配置，并开始执行 {check_name} 签到----------")
            for check_itme in check_info.get(one_check.lower(),[]):
                try:
                    msg = check_func(check_itme).main()
                    content_list.append(f"【{check_name}】\n{msg}")
                    print(f"【{check_name}】\n{msg}")
                except Exception as e:
                    content_list.append(f"【{check_name}】\n{e}")
                    print(check_name, e)
        else:
            print(f"----------未检测到正确的配置，并跳过执行 {check_name} 签到----------")

    if motto:
        try:
            content_list.append(Motto().main())
        except Exception as e:
            print(e)
    
    push_msg(content_list,notice_info)

 
if __name__ == "__main__":
    main()

