import logging
import requests
import logging
from itemadapter import ItemAdapter
from foody.check_DB import check_data
class FoodyPipeline:

    def open_spider(self, spider):
        self.api = 'http://0.0.0.0/drinks'


    def process_item(self, item, spider):
        data = ItemAdapter(item).asdict()
        if check_data(data['drink_names'], data['store_names']):
            logging.warn("[!] DATA already exists !!")
        else:
            requests.post(self.api, json=data)
            logging.info("Add the data in table")
        return item