# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class NenmoPipeline(ImagesPipeline):
##    def process_item(self, item, spider):
##        with open ('qwer.txt','a') as f:
##            f.write(f'{item}\n')
##          
##            return item
    def get_media_requests(self,item,info):
        
        
        yield scrapy.Request(url = item['image_url'][0])
            
    
        
    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no image")
        return item
