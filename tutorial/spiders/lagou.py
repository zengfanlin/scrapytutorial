import json

import scrapy

from tutorial.transCookie import transCookie


class DmozSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "https://www.lagou.com",

    ]

    def start_requests(self):
        # body 为响应体 而不是html中的body标签
        post_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%9D%AD%E5%B7%9E&needAddtionalResult=false'
        cookie = "JSESSIONID=ABAAABAAAIAACBID52C169963C8F9147166B172657D40B1; _ga=GA1.2.2116330701.1551238301; user_trace_token=20190227113140-324edeb1-3a40-11e9-9568-525400f775ce; LGUID=20190227113140-324ee13a-3a40-11e9-9568-525400f775ce; index_location_city=%E6%9D%AD%E5%B7%9E; TG-TRACK-CODE=search_code; _putrc=461BD58FF1DA94C8123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B71509; gate_login_token=9ef5a40aef6f4333c9f61a6488dded5e990777876b8016a05b5e573414e2d5ab; hasDeliver=0; LGRID=20190227141420-ebbd21e5-3a56-11e9-971e-525400f775ce; SEARCH_ID=23e675c1b47144d3ab3687f16fd3dd9c"

        trans = transCookie(cookie)
        print(trans.stringToDict())
        dict1 = {"first": 'true', "pn": "1", 'kd': 'java'}
        yield scrapy.Request(
            url=post_url,
            method='POST',
            body=json.dumps(dict1),
            cookies=trans.stringToDict(),
            headers={'Content-Type': 'application/json', 'Connection': 'keep-alive', 'host': 'www.lagou.com'},
            callback=self.parse
        )

    def parse(self, response):
        datas = json.loads(response.body.decode())  # ['content']['positionResult']['result']
        print(datas)
        # for data in datas:
        #     print(data['companyFullName'] + str(data['positionId']))
