#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import random



def loadPage(url, filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename : 处理的文件名
    """
    print "正在下载 " + filename
    ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    ]

    user_agent = random.choice(ua_list)
    request = urllib2.Request(url)
    request.add_header("User-agent", user_agent)
    print request.get_header("User-agent")
    return urllib2.urlopen(request).read()

def wirtePage(html, filename):
    """
        作用：将html内用写到本地
        html：服务器相应文件内容
        filename : 处理的文件名
    """
    print "正在保存 " + filename
    with open(filename, "w") as f:
        f.write(html)
    print "-" * 30

def tibaSpider(url, beginPage, endpage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    for page in range(beginPage, endpage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)

        html = loadPage(fullurl, filename)
        wirtePage(html, filename)


if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endpage = int(raw_input("请输入结束页："))
    url = "http://tieba.baidu.com/f"

    key = urllib.urlencode({"kw": kw})
    fullurl = url + '?' + key
    tibaSpider(fullurl, beginPage, endpage)


