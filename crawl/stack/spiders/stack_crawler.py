# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    # pattern = re.compile(r"[a-zA-Z]+")
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'https://stackoverflow.com/questions/tagged/python?page=1&sort=frequent'
    ]

    #rules = (
    #    Rule(LinkExtractor(allow=r'questions\?page=[0-100]&sort=frequent'),
    #         callback='parse', follow=True),
    #)

    def parse(self, response):
        for href in response.xpath('//div[@class="question-summary"]'):
            url = response.urljoin(href.xpath('div/h3/a/@href').extract()[0])
            yield scrapy.Request(url, callback=self.parse_item)
        next_page = response.xpath('//a[@rel="next"]/@href').extract()[0]
        next_page = response.urljoin(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)


    def parse_item(self, response):
        yield {
            'title': response.xpath('//h1/a/text()').extract()[0],
            'url': response.url,
            'tags': response.xpath('//a[@class="post-tag"]/text()').extract(),
            'status': {
                'votes': response.xpath(
                    '//div[@class="vote"]/span/text()').extract()[0],
                'favorite_count': response.xpath(
                    '//div[@class="favoritecount"]/b/text()').extract()[0],
                'answers': response.xpath(
                    '//span[@itemprop="answerCount"]/text()').extract()[0],
                'views': response.xpath(
                    '//td/p[@class="label-key"]/b/text()').extract()[1][:-6],
            },
            'user': response.xpath('//div[@class="user-details"]//a[starts-with(@href,"/users/")]/text()').extract()
        }
