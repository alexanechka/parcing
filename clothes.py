import scrapy


class ClothesSpider(scrapy.Spider):
    name = 'clothes'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    def parse(self, response):
        cards = response.xpath("//div[@class='card']")
        print('cards', cards)

        for card in cards:
            
            yield {
                'title': card.xpath(".//h4/a/text()").get(),
                'price': card.xpath(".//h5/text()").get(),
                'image': response.urljoin(card.xpath(".//a/img/@src").get()),
                'description': response.urljoin(card.xpath(".//a/@href").get())
            }

        next_page = response.xpath("//a[contains(., 'Next')]/@href").get()
        #print('next', next_page)

        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)


