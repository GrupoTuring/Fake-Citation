import scrapy

class CitationSpider(scrapy.Spider):
    name = 'citation'
    start_urls = ['https://www.aosfatos.org/']
    allowed_domains= ['aosfatos.org']
    def parse(self, response):
        links_categories = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
        for link in links_categories:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_category
            )

    def parse_category(self, response):
        news = response.css('.card::attr(href)').getall()
        for news_url in news:
            yield scrapy.Request(
                response.urljoin(news_url),
                callback = self.parse_news
            )
        pagination = response.css('.pagination a::attr(href)').getall()
        for page in pagination:
            yield scrapy.Request(
                response.urljoin(page),
                callback=self.parse_category
            )

    def parse_news(self, response):
        #'extrair o fato checado', data, citação, status e url
        news_title = response.css('article h1::text').get()
        #date = str(response.css('p.published_date::text').get()).strip()
        quotes = response.css('article blockquote p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quote.xpath('./parent::blockquote/preceding-sibling::figure//figcaption//text()').getall()
            if "\r\n" in status:
                status.remove("\r\n")
            status = status[-1]
            if not status:
                continue
            yield {
                'title': news_title,
                #'datetime': date,
                'citation': quote_text,
                'category': status,
                'url': response.url
            }