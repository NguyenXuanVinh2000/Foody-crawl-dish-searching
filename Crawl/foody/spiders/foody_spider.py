
from scrapy.loader import ItemLoader
from foody.items import FoodyItem
import scrapy
import json

class FoodySpider(scrapy.Spider):
    name = "foody"
    start_urls = "https://gappapi.deliverynow.vn/api/delivery/get_browsing_ids"
    
    def __init__(self):
        self.rating = None
        self.name_restaurant = None
        self.address = None
        self.headers = {
            'x-foody-api-version': '1',
            'x-foody-app-type': '1004',
            'x-foody-client-id': '',
            'x-foody-client-language': 'vi',
            'x-foody-client-type': '1',
            'x-foody-client-version': '1',
        }
    
    def start_requests(self):
        payload = {
            "sort_type":2,
            "city_id":219,
            "root_category":1000001,
            "root_category_ids":[1000001]
        }
        yield scrapy.Request(self.start_urls,
                            method='POST',
                            headers=self.headers,
                            body=json.dumps(payload),
                            callback=self.parser_list_id)
                            
    def parser_list_id(self,response):
        json_text_list_id_restaurant = response.text
        json_list_id_restaurant = json.loads(json_text_list_id_restaurant)
        list_id_restaurant = json_list_id_restaurant['reply']['delivery_ids']
        for i in range(0, len(list_id_restaurant)):
            url_api_info_restaurant = 'https://gappapi.deliverynow.vn/api/delivery/get_detail?id_type=2&request_id='+str(list_id_restaurant[i])
            request_info_restaurant = scrapy.Request(url_api_info_restaurant,
                                                        method='GET',
                                                        headers=self.headers,
                                                        callback=self.parser_info_restaurant)
            yield request_info_restaurant

            url_api_info_dish = 'https://gappapi.deliverynow.vn/api/dish/get_delivery_dishes?id_type=2&request_id='+str(list_id_restaurant[i])
            request_info_dish = scrapy.Request(url_api_info_dish,
                                                        method='GET',
                                                        headers=self.headers,
                                                        callback=self.parser_info_dish)
            yield request_info_dish


    def parser_info_restaurant(self,response):
        json_text_info_restaurant = response.text
        json_info_restaurant = json.loads(json_text_info_restaurant)
        self.name_restaurant = json_info_restaurant['reply']['delivery_detail']['name']
        self.address = json_info_restaurant['reply']['delivery_detail']['address']
        self.rating = json_info_restaurant['reply']['delivery_detail']['rating']['avg']

    def parser_info_dish(self,response):
        json_text_list_info_dish = response.text
        json_list_info_dish = json.loads(json_text_list_info_dish)
        for info_dish_type in json_list_info_dish['reply']['menu_infos']:
            for info_dish in info_dish_type['dishes']:
                item = ItemLoader(FoodyItem())
                item.add_value('drink_names', str(info_dish['name']))
                item.add_value('prices', str(info_dish['price']['value']))
                item.add_value('ratings', str(self.rating))
                item.add_value('store_names', str(self.name_restaurant))
                item.add_value('address', str(self.address))
                yield item.load_item()
