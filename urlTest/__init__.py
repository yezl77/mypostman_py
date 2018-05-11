# !/usr/bin/python2
# -*- coding:utf-8 -*-
import httputil
import time

def getData(data):
    print data


httpHelper = httputil.HttpHelper()
reqUrl = 'http://172.18.129.64:8080/ye'

httpHelper.setUrl(reqUrl)


# 测试设置头部
def testHeader():
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
    httpHelper.setHeaders(headers)


# 测试设置为长链接
def testKeepAlive():
    httpHelper.serConnectionKeepAlive()


# 测试设置超时时间
def testSetTimeout():
    httpHelper.setTimeOut(200)


#测试Debug收发包日志
def testDebug():
    httpHelper.setDebug()


# 测试put
def testPut():
    putData = {'username': 'yezhenliang', 'password': '1234', 'other': 'urlPut'}
    print "put测试结果：", httpHelper.put(putData)


def testPut2():
    putData = {'username5': 'yezhenliang5', 'password5': '12345', 'other5': 'urlPut5'}
    print "put测试结果：", httpHelper.put(putData)


# 测试Get
def testGet():
    print "get测试结果：", httpHelper.get("username")


# 测试delete
def testDelete():
    delData = {'username': ''}
    print "delete测试结果：", httpHelper.delete(delData)


# 主方法
def main():
    #testSetTimeout()
    #testDebug()
    #testHeader()
    #testKeepAlive()
    testPut()

    time.sleep(10)
    testGet()


    testDelete()

    testGet()


if __name__ == '__main__':
    main()
