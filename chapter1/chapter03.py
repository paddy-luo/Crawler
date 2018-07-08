# -*- coding: UTF-8 -*-
# 利用urllib.urlopen向有道翻译发送数据获得翻译结果

from urllib import request
from urllib import parse
import json
from datetime import datetime

if __name__ == '__main__':

    def getResponse(url, header, formData):
        data = parse.urlencode(formData).encode("utf-8")
        req = request.Request(url, headers=header, data=data)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        return json.loads(html)

    def getLangDetect(url, header, word):
        formData = {}
        formData["query"] = word
        return getResponse(url, header, formData)

    def getTranslateResult(url, header, word):
        formData = {}
        formData["from"] = "en"
        formData["to"] = "zh"
        formData["query"] = word
        formData["transtype"] = "translang"
        formData["simple_means_flag"] = "3"
        formData["sign"] = "262931.57378"
        formData["token"] = "ef017b5c6863c3e5130b1c73f4a555cc"
        return getResponse(url, header, formData)

    header = {}
    header[
        "User-Agent"] = "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    header[
        "cookie"] = "BAIDUID=7EE6075F7669DDA4BFADD70458C87E27:FG=1; PSTM=1524022633; BIDUPSID=CCF0DFB0A9EEAEB80C7E0230FD5F4F0E; __cfduid=dec0a5187e20faa4ca6b403625930396b1527167592; MCITY=-%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSINO=6; H_PS_PSSID=1455_21096_20718; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531052110; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531060457; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"


    langdetect_url = "http://fanyi.baidu.com/langdetect"
    word = "word"
    print(getLangDetect(langdetect_url, header, word))

    v2transApi = "http://fanyi.baidu.com/v2transapi"
    print(getTranslateResult(v2transApi, header, word))





