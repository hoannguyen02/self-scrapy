# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        res_body = json.loads(response.body)
        quotes = res_body.get('quotes')
        for quote in quotes:
            yield {
                'author': quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'text': quote.get('text')
            }

        has_next = res_body.get('has_next')
        if has_next:
            next_page = res_body.get('page') + 1
            yield scrapy.Request(url=f'http://quotes.toscrape.com/api/quotes?page={next_page}', callback=self.parse)
