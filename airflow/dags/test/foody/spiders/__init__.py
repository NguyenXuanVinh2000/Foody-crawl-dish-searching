# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from scrapy.loader import ItemLoader
from foody.items import FoodyItem
from retry import retry
from timeout_decorator import timeout, TimeoutError
import logging
from foody.check_DB import check_data

@retry(TimeoutError, tries=3)
@timeout(10)
def get_with_retry(driver, url):
    driver.get(url)
    
def list_store():
    urls = []
    f = open("/opt/airflow/dags/test/foody/store.txt", "r")
    for x in f:
        urls.append(x)
    return urls
class FoodySpider(scrapy.Spider):
    name = "foody"
    start_urls = list_store()
    def __init__(self):
        self.chrome_options = Options()
       # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--incognito")

    def parse(self, response):


        driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path="/opt/airflow/dags/testfoody/slenium_driver/chromedriver")
        try:
            get_with_retry(driver, response.url)
            time.sleep(3)

            rating = '4.5'
            store_name = driver.find_element_by_css_selector('h1[class="name-restaurant"]').text
            address = driver.find_element_by_css_selector('div[class="address-restaurant"]').text

            last_height = driver.execute_script("return document.documentElement.scrollHeight")
            while True:
                driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
                time.sleep(0.25)
                new_height = driver.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            scroll = last_height // 1500
            if scroll < 1:
                scroll =1
            driver.close()


            driver2 = webdriver.Chrome(chrome_options=self.chrome_options, executable_path="/opt/airflow/dags/testfoody/slenium_driver/chromedriver")
            driver2.get(response.url)
            time.sleep(3)

            lst_drink_name = []
            lst_prices =[]
            lst_status = []
            lst_rating =[]
            lst_store_names = []
            lst_address = []

            for i in range(1,scroll+1):
                for Divs in driver2.find_elements_by_css_selector('div[class="item-restaurant-row"]'):
                    text = Divs.text
                    text =str(text)
                    text = text.replace(",","")
                    text = text.replace("0đ","0")
                    text = text.replace("+","Còn hàng")
                    text2 = text.split("\n")
                    lst_drink_name.append(text2[0])
                    length = len(text2)
                    lst_prices.append(text2[length-2])
                    lst_status.append(text2[length-1])                                                  

                    lst_rating.append(rating)
                    lst_store_names.append(store_name)
                    lst_address.append(address)
                if i == 1:
                    driver2.execute_script("window.scrollTo(0,1500);")
                elif i==2:
                    driver2.execute_script("window.scrollTo(0,3000);")
                elif i==3:
                    driver2.execute_script("window.scrollTo(0,4500);")
                elif i==4:
                    driver2.execute_script("window.scrollTo(0,6000);")
                elif i==5:
                    driver2.execute_script("window.scrollTo(0,7500);")
                elif i==6:
                    driver2.execute_script("window.scrollTo(0,9000);")
                elif i==7:
                    driver2.execute_script("window.scrollTo(0,10500);")
                elif i==8:
                    driver2.execute_script("window.scrollTo(0,12000);")
                elif i==9:
                    driver2.execute_script("window.scrollTo(0,13500);")
                if i == 10:
                    driver2.execute_script("window.scrollTo(0,15000);")
                if i == 11:
                    driver2.execute_script("window.scrollTo(0,16500);")
                elif i==12:
                    driver2.execute_script("window.scrollTo(0,18000);")
                elif i==13:
                    driver2.execute_script("window.scrollTo(0,19500);")
                elif i==14:
                    driver2.execute_script("window.scrollTo(0,21000);")
                elif i==15:
                    driver2.execute_script("window.scrollTo(0,22500);")
                elif i==16:
                    driver2.execute_script("window.scrollTo(0,24000);")
                elif i==17:
                    driver2.execute_script("window.scrollTo(0,25500);")
                elif i==18:
                    driver2.execute_script("window.scrollTo(0,27000);")
                elif i==19:
                    driver2.execute_script("window.scrollTo(0,28500);")
                elif i==20:
                    driver2.execute_script("window.scrollTo(0,30000);")
                time.sleep(1)
            driver2.close()

            check_lst =[]
            for drink_name, price, status, rating, store_name, address in zip(lst_drink_name, lst_prices, lst_status, lst_rating, lst_store_names, lst_address):
                if drink_name not in check_lst:
                    check_lst.append(drink_name)    
                    if check_data(drink_name, store_name):
                        logging.info("[!] DATA already exists !!")
                    else:
                        item = ItemLoader(FoodyItem())
                        item.add_value('drink_names', drink_name)
                        item.add_value('prices', price)
                        item.add_value('statuss', status)
                        item.add_value('ratings', rating)
                        item.add_value('store_names', store_name)
                        item.add_value('address', address)
                        yield item.load_item()
        finally:
            driver.quit()