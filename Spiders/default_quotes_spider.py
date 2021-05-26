import scrapy
from datetime import datetime


class DefaultQuotesSpider(scrapy.Spider):
    name = "default"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    # Things we will parse from each quote
    # Author, text, tags, timestamp, uri

    def parse(self, response):
        ts = datetime.now()
        quotes = response.css("div.quote")
        for quote in quotes:
            yield {
                "text": quote.css("span.text::text").get().translate({ord(i): None for i in '\u201c\u201d'}),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
                "timeStamp": ts,
                "uri": response.request.url
            }
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
