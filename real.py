import scrapy


class QuotesSpider(scrapy.Spider):
    name = "link"
    start_urls = [
        'https://lapor.jogjaprov.go.id/index.php?mod=widget&sub=semuaAspirasi&act=view&typ=html&page=1&keyword=&combo=&display=60&uniq=1619169692779',
    ]

    def parse(self, response):
        for quote in response.css('div.col-xs-12 div.asp-ticket-item div.asp-ticket-body'):
            yield {
                'title': response.urljoin(quote.css('a::attr(href)').get()),
            }
        next_page = response.css('div.pagination a::attr(href)')[-2].get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)