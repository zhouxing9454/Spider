import requests
import re

class DoubanSpider_book:
    def __init__(self):
        self.url="https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={}"  # 共15,以1为递增
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}

    def parse_url(self,url):
        response=requests.get(url,headers=self.headers)
        book_content=response.text
        return book_content;

    def re_complete(self,book_content):
        obj=re.compile(r'<li class="media clearfix">.*?<h2 class="clearfix">.*?<a class="fleft" href=".*?">(?P<book_name>.*?)</a>.*?'
                       r' <p class="subject-abstract color-gray">(?P<author>.*?)/.*?</p>.*?'
                       ,re.S)
        result=obj.finditer(book_content)
        return result;

    def run(self):
        num =1;
        while num<=15:
            book_content = self.parse_url(self.url.format(num))
            result = self.re_complete(book_content)
            for it in result:
                with open('douban_book.txt',"a",encoding='utf-8') as f:
                    f.write(it.group("book_name"))
                    f.write('\n')
                    f.write(it.group("author").strip())
                    f.write('\n')
                    f.write('\n')
            num+=1;


if __name__=="__main__":
    doubanspider_book=DoubanSpider_book()
    doubanspider_book.run()
