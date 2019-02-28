import json

import scrapy
from scrapy.http import Request

from tutorial.items import TutorialItem


class DmozSpider(scrapy.Spider):
    name = "5i5j"
    allowed_domains = ["5i5j.com"]
    start_urls = [
        "https://hz.5i5j.com/ershoufang/n1/",

    ]

    def parse(self, response):
        print(response)
        page_next = response.css('.cPage').css('a::attr(href)').extract_first()

        for site in response.css('.pList li'):
            item = TutorialItem()
            item['title'] = site.css('.listTit').css('a::text').extract()
            item['info'] = site.css('.listX').css('p::text').extract()
            item['price'] = site.css('.listX').css('.jia').css('.redC').css("strong::text").extract()
            yield item
            # yield {
            #     # a标签的文本。
            #     "title": site.css('.listTit').css('a::text').extract(),
            #     "info": site.css('.listX').css('p::text').extract(),
            #     "price":site.css('.listX').css('.jia').css('.redC').css("strong::text").extract()
            #     # "address": site.css('.listX').css('p::text').extract(),
            #     # a标签的连接
            #     # "herf": site.css('a::attr(href)').extract_first()
            # }

        if page_next.strip():
            next_url = 'https://hz.5i5j.com' + page_next
            yield scrapy.Request(next_url, callback=self.parse)
