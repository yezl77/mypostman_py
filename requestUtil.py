# -*- coding:utf-8 -*-

import requests

__metaclass = type


class HttpHelper(object):
    def __init__(self):
        pass

    # session
    __session = requests.session()
    # header
    __reqHeader = {}
    # url
    __reqUrl = ''
    # time
    __reqTimeOut = 0

    def setUrl(self, url):
        self.__reqUrl = url

    def setHeader(self, header):
        self.__reqHeader = header

    def setTimeOut(self, timeout):
        self.__reqTimeOut = timeout

    def serConnectionKeepAlive(self):
        self.__reqHeader["Connection"] = "keep-alive"
        return self

    def post(self, key, putData):
        return self.__session.put(self.__reqUrl+str(key), data=putData,
                                  headers=self.__reqHeader if len(self.__reqHeader) != 0 else None,
                                  timeout=self.__reqTimeOut if self.__reqTimeOut != 0 else None)

    def put(self, key, putData):
        return self.__session.put(self.__reqUrl+str(key), data=putData,
                                  headers=self.__reqHeader if len(self.__reqHeader) != 0 else None,
                                  timeout=self.__reqTimeOut if self.__reqTimeOut != 0 else None)

    def get(self, key):
        res = self.__session.get(self.__reqUrl+str(key),
                                 headers=self.__reqHeader if len(self.__reqHeader) != 0 else None,
                                 timeout=self.__reqTimeOut if self.__reqTimeOut != 0 else None)
        return res.content, res

    def delete(self, key):
        return self.__session.delete(self.__reqUrl+str(key),
                                     headers=self.__reqHeader if len(self.__reqHeader) != 0 else None,
                                     timeout=self.__reqTimeOut if self.__reqTimeOut != 0 else None)

