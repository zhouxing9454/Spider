import requests
import re

class DoubanSpider_book:
    def __init__(self):
        self.url="https://book.douban.com/top250?start={}"  # 225,25递增，0开始的
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

    def parse_url(self,url):
        response=requests.get(url,headers=self.headers)
        page_content=response.text
        return page_content;

    def re_complete(self,page_content):
        obj=re.compile(r'<div class="pl2">.*?<a href=".*?".*?title="(?P<title>.*?)".*?>.*?</a>.*?'
                       r'<p class="pl">(?P<information>.*?)</p>.*?'
                       r'<span class="inq">(?P<assess>)</span>.*?',re.S)
        result=obj.finditer(page_content)
        return result;

    def run(self):
        num=0;
        x=1;
        while num<=225:
            print(x)
            x=x+1;
            page_content=self.parse_url(self.url.format(num))
            result=self.re_complete(page_content)
            for it in result:
                with open('douban_book_top2501.txt',"a") as f:
                    f.write(it.group("title"))
                    f.write('\n')
                    f.write(it.group("information"))
                    f.write('\n')
                    f.write(it.group("assess"))
                    f.write('\n')
                    f.write('\n')
            num+=25;


if __name__=="__main__":
    doubanspider_book=DoubanSpider_book()
    doubanspider_book.run()