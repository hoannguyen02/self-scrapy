import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from tinydeal.spiders.special_offers import SpecialOffersSpider
process = CrawlerProcess(settings=get_project_settings())  # Basically get all settings from settings.py file, then assigned them to settings argument
process.crawl(SpecialOffersSpider) # ~ scrapy crawl special_offers on terminal
process.start()