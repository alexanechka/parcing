import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ClothesDescrSpider(CrawlSpider):
    name = 'clothes_descr'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[contains(., 'Next')]"), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='card']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h3/text()').get()
        item['price'] = response.xpath("//div[@class='card-body']/h4/text()").get()
        item['description'] = response.xpath('//div[@class="card-body"]/p/text()').get()
        item['image'] = response.urljoin(response.xpath('//img/@src').get())

        return item
