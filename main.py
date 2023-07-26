import requests
import time
import random
import json

k=100
num=int(input("请输入请求次数"))
for i in range(num):
    r_num=random.randint(0, 2)
    k=k+1
    if r_num==0:
        get_z=requests.get("https://v1.hitokoto.cn")
        z_jx=json.loads(get_z.text)
        print("mycars[",end="")
        print(k,end="")
        print("]",end="")
        print("=",end="")
        print('"',end="")
        print(z_jx["hitokoto"],end="")
        print('";')
    elif r_num==1:
        get_o=requests.get("https://apiup.tcxone.eu.org/yiyan.php")
        o_jx=json.loads(get_o.text)
        print("mycars[",end="")
        print(k,end="")
        print("]",end="")
        print("=",end="")
        print('"',end="")
        print(o_jx["txt"],end="")
        print('";')
    elif r_num==2:
        get_t=requests.get("https://api.vvhan.com/api/ian")
        print("mycars[",end="")
        print(k,end="")
        print("]",end="")
        print("=",end="")
        print('"',end="")
        print(get_t.text,end="")
        print('";')
    time.sleep(3)
