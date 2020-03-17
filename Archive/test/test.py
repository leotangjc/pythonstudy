# -*- coding: utf-8 -*-

import urllib

url = "http://reg.haibian.com/login/ajax_login"

# 定义请求数据，并且对数据进行赋值
data = {}
data['loginname'] = 'student08qq.com'
data['password'] = '11111'

# 对请求数据进行编码(使用&划分)
data = urllib.urlencode(data)

# 将数据和url进行连接
request = url + '?' + data

requestResponse = urllib.request.urlopen(request)

print(requestResponse.read())
