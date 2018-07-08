# -*- coding: UTF-8 -*-
# 利用urllib.urlopen向有道翻译发送数据获得翻译结果

from urllib import request

if __name__ == '__main__':
    req =  request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    html = response.read()
    html = html.decode('utf-8')
    print(html)
