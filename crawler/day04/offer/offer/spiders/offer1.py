# -*- coding: utf-8 -*-


import scrapy
from offer.items import OfferItem
import json
import time
from scrapy.http.request import Request

class offerSpider(scrapy.Spider):

    name = "offer"

    post_url = [
        # 1
        ('POST',
         'json',
         {"pageNum": '1'},
         "https://be02.bihu.com/bihube-pc/api/content/show/hotArtList",
         'json'),
        # 2
        ('POST',
         None,
         "https://be02.bihu.com/bihube-pc/api/content/queryBoardList",
         'json'),
        # 3
        ('POST',
         'json',
         {"key": "q", "type": []},
         "https://be02.bihu.com/bihube-pc/bihu/search/sug",
         'json'),
        # 4
        ('POST',
         'json',
         {'artId': "1595679878"},
         "https://be02.bihu.com/bihube-pc/api/content/show/getArticle2",
         'json'),
        # 5
        ('GET',
         'https://oss02.bihu.com/article/2019/0326/14_1553584083314_53kXfYcK.txt',
         'txt'),
        # 6
        ('GET',
         "https://static1.bihu.com/bihu-be/api/content/show/getArticle/1355719746",
         'html',
         ),
        # 7
        ('GET',
         "https://static1.bihu.com/bihu-be/api/content/show/getArticle/1070130119",
         'html',
         ),
        # 8
        ('GET',
         "https://static1.bihu.com/bihu-be/api/content/show/getArticle/1099942369",
         'html',
         ),
        # 9
        ('GET',
         "https://static1.bihu.com/bihu-be/api/content/show/getArticle/1222342535",
         'html',
         ),
        # 10
        ('GET',
         "https://cdn.bihu-static.com/bihu-native/favicon.ico",
         "ico",

         ),
     ]

    headers_post = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36",
    }

    headers_get = {
        "Cookie": "UM_distinctid=169b17090811742-0b3b1f8fa50b58-10724c6f-100200-169b170908b59f9",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36",
    }

    def get_request_parameter(self, urls):
        if urls[0] == 'POST':
            method = 'POST'
            headers = self.headers_post
            if urls[1] == 'json':
                url = urls[3]
                body = json.dumps(urls[2])
                meta = urls[4]
            elif urls[1] == None:
                url = urls[2]
                body = None
                meta = urls[3]
            else:
                EOF_Err = -22
                print EOF_Err
                return
        elif urls[0] == 'GET':
            url = urls[1]
            method = 'GET'
            headers = self.headers_get
            body = None
            meta = urls[2]
        else:
            EOF_Err = -21
            print urls[0]
            print EOF_Err
            return
        return {"method": method, "body": body, "url": url, "headers": headers, "meta": meta}

    def start_requests(self):
        for urls in self.post_url:
            item = self.get_request_parameter(urls)

            yield Request(
                url=item['url'],
                method=item['method'],
                body=item['body'],
                headers=item['headers'],
                meta= {"meta": item["meta"]},
                callback=self.parse_page)

    def parse(self, response):
        pass

    def parse_page(self, response):
        item = OfferItem()
        item['url'] = response.request.url
        item['meta'] = response.meta["meta"]

        if item['meta'] == "ico":
            item['content'] = response.body
        elif item['meta'] == "json"\
            or item['meta'] == "txt"\
            or item['meta'] == "html":
            item['content'] = response.text
        return item


