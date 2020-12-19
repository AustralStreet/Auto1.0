# -*- coding:utf-8 -*-
import xlrd
from TestRequest import TestPostRequest
from TestRequest import TestGetRequest
from testdata.getpath import GetTestDataPath


testdata = xlrd.open_workbook(GetTestDataPath())







testurl="http://127.0.0.1:8000"
def post_vote():
    try:
        table = testdata.sheets()[1]
        for i in range(3,5):
            choice=table.cell(i,0).value
            status=table.cell(i,1).value
            qiwang = table.cell(i, 2).value
            hdata={
                'choice':int(choice)
            }
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testvote"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestPostRequest(testurl+'/polls/1/vote/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
    except Exception as e:
        print(e)
# post_vote()

def get_polls():
    try:
        table = testdata.sheets()[1]
        for i in range(13,14):
            status = table.cell(i, 0).value
            qiwang = table.cell(i, 1).value
            hdata=""
            header = {
                'content-type': "application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testpolls"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest(testurl+'/polls/1/',hdata,header,testcaseid,testname,testhope,fanhuitesthpe,"status")
    except Exception as e:
        print(e)

# get_polls()

def post_login():
    try:
        table = testdata.sheets()[3]
        for i in range(3,5):
            username = table.cell(i,0).value
            password = table.cell(i,1).value
            status = table.cell(i,2).value
            qiwang = table.cell(i,3).value
            hdata = {
                    'username':username ,
                    'password':int(password)
                     }
            header = {
                    'content-type': "application/x-www-form-urlencoded"
                }
            testcaseid="1-1"
            testname="testlogin"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestPostRequest("http://127.0.0.1:8000/polls/login/",hdata,header,testcaseid,testname,testhope,fanhuitesthpe)
    except Exception as e:
        print(e)

# post_login()


def get_news():
    try:
        table = testdata.sheets()[4]
        for i in range(3,4):
            status = table.cell(i,0).value
            qiwang = table.cell(i,1).value
            hdata = ""
            header = {
                    'content-type': "application/x-www-form-urlencoded"
                }
            testcaseid="1-2"
            testname="testnews"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest("https://www.apiopen.top/journalismApi",hdata,header,testcaseid,testname,testhope,fanhuitesthpe,'code')
    except Exception as e:
        print(e)
# get_news()


def get_joke():
    try:
        table = testdata.sheets()[4]
        for i in range(13,15):
            type = table.cell(i, 0).value
            page = table.cell(i, 1).value
            status = table.cell(i,2).value
            qiwang = table.cell(i,3).value
            hdata = {
                    'type':type,
                    'page':int(page)
            }
            header = {
                    'content-type': "application/x-www-form-urlencoded"
                }
            testcaseid="1-3"
            testname="testjoke"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest("https://www.apiopen.top/satinApi",hdata,header,testcaseid,testname,testhope,fanhuitesthpe,'code')
    except Exception as e:
        print(e)
# get_joke()


def get_novel():
    try:
        table = testdata.sheets()[4]
        for i in range(21,22):
            name = table.cell(i, 0).value
            status = table.cell(i,1).value
            qiwang = table.cell(i,2).value
            hdata = {
                    'name': name
            }
            header = {
                    'content-type': "application/x-www-form-urlencoded"
                }
            testcaseid="1-4"
            testname="get_novel"+testcaseid
            testhope=str(int(status))
            fanhuitesthpe=qiwang
            r=TestGetRequest("https://www.apiopen.top/novelSearchApi",hdata,header,testcaseid,testname,testhope,fanhuitesthpe,'code')
    except Exception as e:
        print(e)
#get_novel()
