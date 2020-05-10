from scrapy import cmdline

spider_list = ["corona"]
scraper_name = spider_list[0]

cmdline.execute(f"scrapy crawl {scraper_name}".split())
