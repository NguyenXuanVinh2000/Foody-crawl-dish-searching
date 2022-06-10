import requests
from itemadapter import ItemAdapter

class FoodyPipeline:

    def open_spider(self, spider):
        self.api = 'http://0.0.0.0/drinks'


    def process_item(self, item, spider):
        data = ItemAdapter(item).asdict()
        requests.post(self.api, json=data)
        return item