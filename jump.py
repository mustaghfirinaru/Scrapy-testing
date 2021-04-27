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
