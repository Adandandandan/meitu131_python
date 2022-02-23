import scrapy
from nenmo.items import NenmoItem
import re
class NenSpider(scrapy.Spider):
    name = 'nen'
    allowed_domains = []
    start_urls = ["https://www.meitu131.net/meinv"]

    def parse(self, response):
        html_urls = response.xpath('/html/body/div[1]/div[2]/ul/li/div[1]/a/@href').extract()
        for html_url in html_urls:
            html_url = f'https://www.meitu131.net{html_url}'
            print(html_url)
            yield scrapy.Request(url = html_url ,callback = self.parse0 )

            
        new_url = response.xpath('//*[@id="pages"]/a[text()="下一页"]/@href').extract_first()
        if new_url:
            yield response.follow(url = new_url,callback = self.parse)
        

    def parse0(self,response):
            
               
        item = NenmoItem()
        item['image_url'] = response.xpath('//*[@id="main-wrapper"]/div[2]/p/a/img/@src').extract()
               
        yield item
        new_image = response.xpath('//*[@id="pages"]/a[text()="下一页"]/@href').extract_first()
        print(new_image)
        if new_image:
            new_image = f'https://www.meitu131.net{new_image}'  
            yield response.follow(url = new_image,callback = self.parse0)  
                
    
        
        

    
