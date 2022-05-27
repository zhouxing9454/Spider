from urllib import request, parse
import json
import jsonpath
import requests
import os


def DuiTang(keyword, keynum):
    name = 1  # 拿来记录获取的顺序，便于对下载下来的文件进行命名

    # 在当前目录下创建文件夹
    try:
        os.mkdir(r'堆糖' + keyword + '下载')
    except Exception:
        pass
    finally:
        os.chdir(r'堆糖' + keyword + '下载')

    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw='
    form = parse.quote(keyword)  # 动态分析中，需要把keyword转化为网页编码所需要的形式.
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    for page in range(1, int(keynum)):
        # Fin_url = url+form+'&type=feed&start='+str(page*24)+'.json'
        req = request.Request(
            url=url + form + '&type=feed&include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,like_id,sender,album,reply_count,favorite_blog_id&_type=&start=' + str(
                page * 24) + '&_=' + str(1540109911555 + page), headers=headers)
        # 因为不清楚url中每部分的具体含义，所以中间的一部分进行保留，但按理来说，其应该没有价值
        # 最后的两组不同的数字，缺一不可，只有一个，就不能刷新成功
        # 一个是24*i，另一个每次都不一样，这里只取某一次刷新时候获得的值，目前还没观察到底每次刷新时值的不同有什么规律

        response = request.urlopen(req)
        # 取出json文件里的内容，返回的格式是字符串
        html = response.read()
        # 把json形式的字符串转换成python形式的Unicode字符串
        unicodestr = json.loads(html)

        # python形式的列表
        url_list = jsonpath.jsonpath(unicodestr, "$..path")
        for li in url_list:
            try:
                document = requests.get(url=li, headers=headers)
                filename = keyword + str(name) + '.jpeg'
                name = name + 1
                with open(filename, 'wb') as f:
                    f.write(document.content)
                    print('文件 ' + filename + '已下载完成！')
            except Exception:
                print('文件 ' + filename + ' 下载失败并忽略！')
                pass


if __name__ == '__main__':
    keyword = input("Input key word: ")
    page= input("Input the pages:")
DuiTang(keyword,page)

