# !/usr/bin/python2
# -*- coding:utf-8 -*-
import requestUtil
import time, threading


t_objs = []   #线程容器


def testSetUrl(httpHelper):
    reqUrl = 'http://172.18.129.64:8080/'
    httpHelper.setUrl(reqUrl)


# 测试设置头部
def testHeader(httpHelper):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
               'Content-Type': 'application/form-urlencode'}
    httpHelper.setHeader(headers)


# 测试设置为长链接
def testKeepAlive(httpHelper):
    httpHelper.serConnectionKeepAlive()


# 测试设置超时时间
def testSetTimeout(httpHelper):
    httpHelper.setTimeOut(60)  # second


# 测试put
def testPut(httpHelper):
    key = 'username'
    putData = 'admins'
    res = httpHelper.put(key, putData)
    # print "put request 头部:", res.request.headers
    # print "put response 头部:", res.headers, "status: ", res.status_code


# 测试Get
def testGet(httpHelper):
    key = 'username'
    result, res = httpHelper.get(key)
    print "result:", result
    # print "get request 头部:", res.request.headers
    # print "get response 头部:", res.headers, "status: ", res.status_code


# 测试delete
def testDelete(httpHelper):
    key = 'username'
    res = httpHelper.delete(key)
    # print "delete request 头部:", res.request.headers
    # print "delete response 头部:", res.headers, "status: ", res.status_code


# 主方法
def main():
    httpHelper = requestUtil.HttpHelper()

    #设置连接url,timeout,header参数
    testSetUrl(httpHelper)
    testSetTimeout(httpHelper)
    testHeader(httpHelper)

    #强制设置长连接，但不设置也是默认为长连接
    #testKeepAlive(httpHelper)

    #测试put方法
    testPut(httpHelper)

    time.sleep(30)

    testGet(httpHelper)

    testDelete(httpHelper)

    #testGet(httpHelper)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=main)
        t.start()
        t_objs.append(t)

    for t in t_objs:
        t.join()



