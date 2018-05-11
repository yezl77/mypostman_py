# -*- coding: utf-8 -*-

import sys
import time
import threading
import requests
import random
import logging
import requestUtil

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='测试脚本日志.log',
                    filemode='w')


thread_count = 2        # 单次并发数量
request_interval = 0.2  # 请求间隔(秒)
test_count = 100        # 指定测试次数
t_objs = []             # 存线程实例

now_count = 1

lock_obj = threading.Lock()


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
    httpHelper.setTimeOut(20)  # second


# 测试put
def testPut(httpHelper):
    key = 'username'
    putData = '叶镇亮'
    res = httpHelper.put(key, putData)
    # print "put request 头部：", res.request.headers
    # print "put response 头部：", res.headers, "status: ", res.status_code


# 测试Get
def testGet(httpHelper):
    key = 'username'
    result, res = httpHelper.get(key)
    print "结果：", result
    # print "get request 头部：", res.request.headers
    # print "get response 头部：", res.headers, "status: ", res.status_code


# 测试delete
def testDelete(httpHelper):
    key = 'username'
    res = httpHelper.delete(key)
    # print "delete request 头部：", res.request.headers
    # print "delete response 头部：", res.headers, "status: ", res.status_code


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

    testGet(httpHelper)

    testDelete(httpHelper)

    testGet(httpHelper)



def send_http():
    global now_count
    global urls
    url = urls[random.randint(0,len(urls)-1)]
    httpClient = None

    try:
        httpClient = requests.request('get',url)

        print('返回码:',str(httpClient.status_code))
        print('返回数据:',httpClient.text)
        #print('返回原始数据:',httpClient.raw.read)

        logging.info('返回码:' + str(httpClient.status_code))
        logging.info('返回数据:' + httpClient.text)

        sys.stdout.flush()
        now_count += 1

    except Exception as e:
        print(e)
        logging.info(e)

    finally:
        if httpClient:
            httpClient.close()


def test_func(run_count):
    global now_count
    global request_interval
    global lock_obj
    cnt = 0

    while cnt < run_count:
        lock_obj.acquire()
        print('')
        print('***************************请求次数:' + str(now_count) + '*******************************')
        print('Thread:(%d) Time:%s\n'%(threading.get_ident(), time.ctime()))

        logging.info('')
        logging.info('***************************请求次数:' + str(now_count) + '*******************************')
        logging.info('Thread:(%d) Time:%s\n' % (threading.get_ident(), time.ctime()))

        cnt += 1
        start_time = time.time()
        send_http()
        end_time = time.time() -start_time
        print("*****************请求时间:" + str(end_time) + "*********************")
        sys.stdout.flush()
        lock_obj.release()
        time.sleep(request_interval)

def test(ct):
    global thread_count
    for i in range(thread_count):
        t = threading.Thread(target=test_func,args=(ct,))
        t.start()
        t_objs.append(t)

    for t in t_objs:
        t.join()


if __name__ == '__main__':
    test(test_count)
    # while True:
    #     time.sleep(100)