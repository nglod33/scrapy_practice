import scrapy
from datetime import datetime
import json


class DefaultQuotesSpider(scrapy.Spider):
    name = "scroll"
    start_urls = [
        'https://quotes.toscrape.com/api/quotes?page=1'
    ]

    # Things we will parse from each quote
    # Author, text, tags, timestamp, uri

    def parse(self, response):

        ts = datetime.now()
        json_response = json.loads(response.text)
        has_next = json_response['has_next']
        quotes = json_response["quotes"]

        for quote in quotes:
            yield {
                "text": quote["text"].translate({ord(i): None for i in '\u201c\u201d'}),
                "author": quote["author"]["name"],
                "tags": quote["tags"],
                "timeStamp": ts,
                "uri": response.request.url
            }
            next_page = 'https://quotes.toscrape.com/api/quotes?page=' + str(int(json_response["page"]) + 1)
            if has_next:
                yield response.follow(next_page, callback=self.parse)
