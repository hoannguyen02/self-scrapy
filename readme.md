# Common scrapy cheatsheet
1. Start project: `scrapy startproject project_name`
2. Generate spider: `scrapy genspider spider_name url(ex: google.com)` or `scrapy genspider spider_name -t crawl url(ex: google.com)`
3. Run spider: `scrapy crawl spider_name` or `scrapy crawl spider_name -o filename.(csv or json)`