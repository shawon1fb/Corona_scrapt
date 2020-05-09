# -*- coding: utf-8 -*-
import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['https://www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus//']

    def parse(self, response):
        temp = response.xpath("//table[@id='main_table_countries_today']/tbody[1]/tr")
        print("--------------------------------------------------------------------------")
        print(f"temp length ----------------->>>{len(temp)}")
        print("--------------------------------------------------------------------------")
        for t in temp:
            item = dict()
            item["Country"] = t.xpath(".//a//text()").get()
            item["Total_Case"] = t.xpath(".//td[2]/text()").get()

            yield item
