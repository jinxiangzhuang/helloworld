# -*- coding:utf-8 -*-

import requests
import re

#def readfile(filename):
#   fopen = open(filename,'r')
#   for eachline in fopen:
#   fopen.close()

"""定义获取token方法"""
def get_token(username,password):
    response = requests.get("http://my.233.mistong.com/login/prelogin?callback=jQuery111205653414290805507_1465181153664&sid=2&username=%s&password=%s&fromurl=http://www.233.mistong.com/&isremember=1&_=1465181153665" %(username,password))
    res = response.content
    #return res
    reg = r'\d{8}-\d-.{16}' #正则条件
    token = re.findall(reg,res)
    
    filename = "F:\\useid.dat"
    fopen = open(filename,'r')
    for username in fopen:
        return username
        print username
    fopen.close()
