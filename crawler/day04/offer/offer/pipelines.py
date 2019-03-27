# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import scrapy
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline

class OfferPipeline(object):
    count = 1
    prefix = ["web", "app"]

    def process_item(self, item, spider):
        filename = self.prefix[0] + str(self.count) + "." + item["meta"]
        file = open("image/" + filename, "w")

        if item['meta'] == "ico":
            file.write(item['content'])
        elif item['meta'] == "json"\
            or item['meta'] == "txt"\
            or item['meta'] == "html":
            file.write(item['url'].encode("utf-8"))
            file.write('\n' * 3)
            file.write(item['content'].encode("utf-8"))
        file.close()

        self.count += 1
        if self.count == 6:
            self.prefix[0], self.prefix[1] = self.prefix[1], self.prefix[0]
        return item