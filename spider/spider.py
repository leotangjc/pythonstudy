# -*- coding: utf-8 -*-

from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/fortnite?pdt=1.27.psbar-re.2.555hmqlul05'
    root_parrern = '<div class="video-info">[\s\S]*?</div>'
    
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
        
        

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_parrern, htmls)
        print(root_html[0])
        a = 1


    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


spider = Spider()
spider.go()