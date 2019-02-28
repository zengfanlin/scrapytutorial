import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://site.baidu.com/cool.html",

    ]

    def parse(self, response):
        # body 为响应体 而不是html中的body标签
        print(response.status)
        # print(response.body.decode(response.encoding))
        # 获取响应头
        # print(response.headers)
        # 获取当前状态
        for site in response.css(' .r30 a'):

            yield {
                # a标签的文本。
                "text": site.css('a::text').extract(),
                # a标签的连接
                # "herf": site.css('a::attr(href)').extract_first()
            }
