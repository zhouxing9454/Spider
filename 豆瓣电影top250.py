import requests
import re


class DoubanSpider_movie:
    def __init__(self):
        self.url="https://movie.douban.com/top250?start={}&filter="  # 225,25递增
        self.headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

    def parse_url(self,url):
        response=requests.get(url,headers=self.headers)
        page_content=response.text
        return page_content;

    def re_complete(self,page_content):
        obj=re.compile(r'<li>.*?<div class="item">.*? <span class="title">(?P<name>.*?)'
                       r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                       r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?',re.S)
        result=obj.finditer(page_content)
        return result;

    def run(self):
        num=0;
        while num<=225:
            page_content=self.parse_url(self.url.format(num))
            result=self.re_complete(page_content)
            for it in result:
                with open('douban_movie_top250.txt',"a") as f:
                    f.write(it.group("name"))
                    f.write('\n')
                    f.write(it.group("score"))
                    f.write('\n')
                    f.write(it.group("year").strip())
                    f.write('\n')
                    f.write('\n')
            num+=25;

if __name__=="__main__":
    doubanspider=DoubanSpider_movie()
    doubanspider.run()
