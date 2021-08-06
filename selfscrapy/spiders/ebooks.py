import scrapy
from scrapy.exceptions import CloseSpider
import json

class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    INCREMENTED_BY = 12
    offset = 0
    start_urls = [f'https://openlibrary.org/subjects/picture_books.json?limit=12']

    def parse(self, response):
        if response.status == 500:
            raise CloseSpider('Reached the last page.')
        res_body = json.loads(response.body)
        ebooks = res_body.get('works')
        for ebook in ebooks:
            yield {
                'title': ebook.get('title'),
                'subject': ebook.get('subject')
            }
        self.offset += self.INCREMENTED_BY
        yield scrapy.Request(url=f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}', callback=self.parse)
