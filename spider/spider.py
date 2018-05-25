# -*- coding: utf-8 -*-

from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/r6?pdt=1.24.s1.30.1ebrm2qdknv'
    
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        a = 1

    def go(self):
        self.__fetch_content()


spider = Spider()
spider.go()