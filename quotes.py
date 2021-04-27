import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://lapor.jogjaprov.go.id/index.php?mod=widget&sub=semuaAspirasi&act=view&typ=html&mmId=114',
    ]

    def parse(self, response):
        for quote in response.css('div.col-xs-12 div.asp-ticket-item div.asp-ticket-body'):
            # innerpage = response.urljoin(response.css('div.asp-ticket-body a::attr(href)').get())
            # yield scrapy.Request(innerpage, callback=self.parse)
            yield {
                'title': quote.css('div.title::text').get(),
                'desc': quote.css('div.main-content::text').get(),
            }

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)