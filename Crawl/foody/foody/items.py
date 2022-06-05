# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import  TakeFirst


class FoodyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    drink_names = scrapy.Field(output_processor=TakeFirst())
    prices = scrapy.Field(output_processor=TakeFirst())
    statuss = scrapy.Field(output_processor=TakeFirst())
    ratings = scrapy.Field(output_processor=TakeFirst())
    store_names = scrapy.Field(output_processor=TakeFirst())
    address = scrapy.Field(output_processor=TakeFirst())
    #pass
