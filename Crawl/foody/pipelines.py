import logging
import requests
import logging
from itemadapter import ItemAdapter
from foody.check_DB import check_data
class FoodyPipeline:

    def open_spider(self, spider):
        self.api_insert = 'http://0.0.0.0/drinks'
        self.api_update = 'http://0.0.0.0/drinks/update/'


    def process_item(self, item, spider):
        data = ItemAdapter(item).asdict()
        if check_data(data['drink_names'], data['store_names']):
            api = self.api_update + data['drink_names'] +"_"+ data['store_names']
            requests.put(api, json=data)
            logging.info("Update data in table")

        else:
            requests.post(self.api_insert, json=data)
            logging.info("Add the data in table")
        return item