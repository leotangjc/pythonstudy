# -*- coding: utf-8 -*-
# g = (x * x for x in range(10))
# for n in g:
#     print(n)

import requests
import json





# def send_post(url, data):
#     res = requests.post(url = url,data = data).json()
#     # return res.json()
#     return json.dumps(res, indent=2, sort_keys=True)
# print(send_post(url, data))




class RunMain:
    
    def __init__(self, url, method, data = None):
        self.res = self.run_main()
    def send_post(self, url, data):
        res = requests.post(url = url,data = data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_get(self, url, data):
        res = requests. get(url = url,data = data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(url, method):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res
        
if __name__ == '__main__':
    url = 'http://....'
    data = {
        'username':'mushishi',
        'passwoed':'111111'
    }
    run = RunMain(url, 'GET', data)
    print(run.res)
#     print(run_main(url, 'GET', data))




