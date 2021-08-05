# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TopBestMoviesSpider(CrawlSpider):
    name = 'top_best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="lister-item-header"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='(//a[contains(@class,"next-page")])[2]')),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath('//div[contains(@class, "TitleBlock__TitleContainer")]/h1/text()').get(),
            'year': response.xpath('//div[contains(@class, "TitleBlock__TitleContainer")]//span/text()').get(),
            'duration': response.xpath('//div[contains(@class, "TitleBlock__TitleContainer")]//li[3]/text()').get(),
            'rating': response.xpath('//div[contains(@class,"Hero__MediaContentContainer")]//span[contains(@class, "AggregateRatingButton__RatingScore")]/text()').get(),
            'movie_url': response.url,
        }
