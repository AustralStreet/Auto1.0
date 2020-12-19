"""
@Auth ：clover
@File ：test_login.py
@Time ：2020/12/18 0018 
"""

import xlrd
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath


testdata = xlrd.open_workbook(GetTestDataPath())


# testurl="http://api.baijiantest.com/memberInterfaces/v1.0/applyEmployee"
testurl="http://192.168.5.10/oauth/token"

def post_token():
    """
    获取token信息
    """
    try:
        table = testdata.sheets()[5]
        for i in range(3,5):
            grant_type = table.cell(i,0).value
            scope = table.cell(i,1).value
            username = table.cell(i,2).value
            password = table.cell(i,3).value
            status = table.cell(i,4).value
            qiwang = table.cell(i,5).value
            hdata = {
                    'grant_type':grant_type ,
                    'scope':str(scope),
                    'username': str(username),
                    'password': int(password)
                     }
            header = {
                    'content-type': "application/x-www-form-urlencoded",
                    'APP-CLIENT-SECURT':"Y2xpZW50OjEyMzQ1Ng=="
                }
            testcaseid="1-1"
            testname="test_token"+testcaseid
            testhope=str(status)
            fanhuitesthpe=qiwang
            r=TestPostRequest(testurl,hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
    except Exception as e:
        print(e)
post_token()
