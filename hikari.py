import scrapy


class hikarinoakari(scrapy.Spider):
    name = "hikarilink"
    start_urls = [
        'https://hikarinoakari.com/',
    ]

    def parse(self, response):
        post_page_links = response.css('div.td-module-thumb a::attr(href)')
        yield from response.follow_all(post_page_links, self.parse_author)

        pagination_links = response.css('div.page-nav  a::attr(href)')[-1]
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        yield {
            'title': response.css('h1.entry-title::text').get(),
        }

# class hikarinoakari(scrapy.Spider):
#     name = "hikarilink"
#     start_urls = [
#         'https://hikarinoakari.com/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.td-module-thumb'):
#             yield {
#                 'link': response.urljoin(quote.css('a::attr(href)').get()),
#             }
#         next_page = response.css('div.page-nav  a::attr(href)')[-1].get()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)