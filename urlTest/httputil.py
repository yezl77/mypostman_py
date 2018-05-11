# -*-coding:utf-8 -*-
import urllib2
import json

__metaclass = type


class HttpHelper(object):
    def __init__(self):
        pass

    name = 'http helper'
    # header
    __reqHeader = {}
    # url
    __reqUrl = ''
    # time
    __reqTimeOut = 0

    # 构建Get请求
    def __buildGetRequest(self):
        if len(self.__reqHeader) == 0:
            request = urllib2.Request(url=self.__reqUrl)
        else:
            request = urllib2.Request(url=self.__reqUrl, headers=self.__reqHeader)
        return request

    # 构建post,put,delete请求
    def __buildPostPutDeleteRequest(self, postData):
        if len(self.__reqHeader) == 0:
            request = urllib2.Request(url=self.__reqUrl, data=postData)
        else:
            request = urllib2.Request(url=self.__reqUrl, headers=self.__reqHeader, data=postData)
        return request

    # 处理response
    def __handleResponse(self, request):
        try:
            if self.__reqTimeOut == 0:
                res = urllib2.urlopen(request)
            else:
                res = urllib2.urlopen(request, timeout=self.__reqTimeOut)
            return res.read()
        except urllib2.HTTPError, e:
            return e.code

    # 添加header
    def setHeaders(self, headers):
        self.__reqHeader = headers
        return self

    def serConnectionKeepAlive(self):
        self.__reqHeader["Connection"] = "keep-alive"
        return self

    # 添加url
    def setUrl(self, url):
        self.__reqUrl = url
        return self

    # 添加超时
    def setTimeOut(self, time):
        self.__reqTimeOut = time
        return self

    # 是否debug
    def setDebug(self):
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler, httpsHandler)
        urllib2.install_opener(opener)
        return self

    # get请求
    def get(self, key):
        request = self.__buildGetRequest()
        res = self.__handleResponse(request)
        print res
        try:
            json_to_python = json.loads(res)
            return json_to_python[key]
        except TypeError:
            return "error"

    # post请求
    def post(self, postData):
        request = self.__buildPostPutDeleteRequest(postData=postData)
        self.__handleResponse(request)
        return "success"

    # put请求
    def put(self, putData):
        request = self.__buildPostPutDeleteRequest(postData=json.dumps(putData))
        request.get_method = lambda: 'PUT'
        self.__handleResponse(request)
        return "success"

    # delete请求
    def delete(self, putData):
        request = self.__buildPostPutDeleteRequest(postData=json.dumps(putData))
        request.get_method = lambda: 'DELETE'
        self.__handleResponse(request)
        return "success"
