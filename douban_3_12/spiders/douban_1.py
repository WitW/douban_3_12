# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request
from douban_3_12.items import Douban312Item

class Douban1Spider(scrapy.Spider):
    name = 'douban_1'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    def parse(self, response):
        # print(response.text)
        selector = Selector(response)
        next_url = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()[0]
        # print(next_url)
        # // *[ @ id = "content"] / div / div[1] / ol / li[1] / div / div[2] / div[1] / a
        movie_pages = selector.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href').extract()
        for movie_page in movie_pages:
            # print(movie_page)
            yield Request(movie_page,callback=self.getMovieDetail,dont_filter=True)
        yield Request(self.allowed_domains[0]+next_url,callback=self.parse,dont_filter=True)

    def getMovieDetail(self,response):
        item = Douban312Item()
        selector = Selector(response)
        item["movie_name"] = selector.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item["rating_num"] = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item["movie_type"] = selector.xpath('//*[@id="info"]/span[5]/text()').extract()
        item["watch_num"] = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()

        yield item


