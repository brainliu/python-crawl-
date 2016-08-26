#in the cmd 
scrapy startproject tutorial
#编辑在tutorial目录下的items.py文件
from scrapy.item import Item, Field 
class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()
#将其命名为dmoz_spider.py并保存在tutorial\spiders目录下   
from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)
scrapy crawl dmoz
