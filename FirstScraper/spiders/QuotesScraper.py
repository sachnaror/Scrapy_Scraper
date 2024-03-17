import csv

import scrapy


class QuotesScraperSpider(scrapy.Spider):
    name = "QuotesScraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath(
            "/html/body/div/div[2]/div[1]/div/span[1]/text()").extract()
        authors = response.xpath(
            "/html/body/div/div[2]/div[1]/div/span[2]/small/text()").extract()

        # Open the CSV file for writing
        with open('/Users/homesachin/Desktop/zoneone/practice/sachin.csv', 'w', newline='') as csvfile:
            fieldnames = ['quote', 'written by']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for quote, author in zip(quotes, authors):
                quote_detail = {
                    "quote": quote.strip(),
                    "written by": author.strip()
                }
                writer.writerow(quote_detail)
