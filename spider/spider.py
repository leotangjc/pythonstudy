# -*- coding: utf-8 -*-
import re

from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/fortnite?pdt=1.27.psbar-re.2.555hmqlul05'
    root_parrern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?</span>)'
    
    def __fetch_content(self):
        r = request.urlopen(Spider.url) # 使用方法读取指定页面，并将其生成一个对象
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8') #将读取到的网页编码转为utf-8格式
        return htmls
        
        

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_parrern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        # print(anchors)
        a = 1

    def __refine(self, anchors):
        l = lambda anchor :{'name':anchor['name'][0].strip()}

    def go(self):  #入口方法
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__refine(anchors)


spider = Spider() #实例化
spider.go() #调用入口方法