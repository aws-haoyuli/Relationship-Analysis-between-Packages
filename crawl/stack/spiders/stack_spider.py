# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'http://stackoverflow.com/questions?pagesize=50&sort=frequent',
    ]


    def parse(self, response):
        questions = Selector(response).xpath(
            '//div[@class="question-summary"]'
        )

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'div/h3/a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'div/h3/a[@class="question-hyperlink"]/@href').extract()[0]
            item['tags'] = question.xpath(
                 'div/div/a[@class="post-tag"]/text()').extract()
            votes = question.xpath(
                'div/div/div[@class="vote"]/div/span/strong/text()'
            ).extract()[0]
            answers = question.xpath(
                 'div/div/div[@class="status answered-accepted"]/strong/text()'
            ).extract()[0]
            views = question.xpath(
                'div/div[@class="views supernova"]/@title'
            ).extract()[0]
            item['status'] = dict(votes=votes, answers=answers, views=views)
            yield item
