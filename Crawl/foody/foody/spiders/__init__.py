# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from scrapy.loader import ItemLoader
from foody.items import FoodyItem

def list_store():
    urls = []
    f = open("/home/vinh/PROJECT CTY/Dish_Searching/Crawl/selenium/store.txt", "r")
    for x in f:
        urls.append(x)
    return urls
class FoodySpider(scrapy.Spider):
    name = "foody"
    start_urls = ['https://www.foody.vn/da-nang']


    def parse(self, response):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920x1080")
        urls = list_store()
        for url in urls:
            driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/vinh/PROJECT CTY/Dish_Searching/Crawl/selenium/chromedriver_linux64/chromedriver")
            driver.get(url)
            time.sleep(3)
            rating = 4.5
            store_name = driver.find_element_by_css_selector('h1[class="name-restaurant"]').text
            address = driver.find_element_by_css_selector('div[class="address-restaurant"]').text
            SCROLL_PAUSE_TIME = 0.25
            
            last_height = driver.execute_script("return document.documentElement.scrollHeight")
            while True:
                # for Divs in driver.find_elements_by_css_selector('div[class="item-restaurant-row"]'):
                #     lst.append(Divs.text)
                # Scroll down to bottom
                driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)
            
                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            scroll = last_height // 2000
            if scroll < 1:
                scroll =1
            driver.close()


            driver2 = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/vinh/PROJECT CTY/Dish_Searching/Crawl/selenium/chromedriver_linux64/chromedriver")

            driver2.get(url)
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
                    if text2[1].isdecimal():
                        lst_prices.append(text2[1])
                        lst_status.append(text2[2])
                    else:
                        lst_prices.append(text2[2])
                        lst_status.append(text2[3])
                    lst_rating.append(rating)
                    lst_store_names.append(store_name)
                    lst_address.append(address)
                if i == 1:
                    driver2.execute_script("window.scrollTo(0,2000);")
                elif i==2:
                    driver2.execute_script("window.scrollTo(0,4000);")
                elif i==3:
                    driver2.execute_script("window.scrollTo(0,6000);")
                elif i==4:
                    driver2.execute_script("window.scrollTo(0,8000);")
                elif i==5:
                    driver2.execute_script("window.scrollTo(0,10000);")
                elif i==6:
                    driver2.execute_script("window.scrollTo(0,12000);")
                elif i==7:
                    driver2.execute_script("window.scrollTo(0,14000);")
                elif i==8:
                    driver2.execute_script("window.scrollTo(0,16000);")
                elif i==9:
                    driver2.execute_script("window.scrollTo(0,18000);")
                if i == 10:
                    driver2.execute_script("window.scrollTo(0,20000);")
                if i == 11:
                    driver2.execute_script("window.scrollTo(0,22000);")
                elif i==12:
                    driver2.execute_script("window.scrollTo(0,24000);")
                elif i==13:
                    driver2.execute_script("window.scrollTo(0,26000);")
                elif i==14:
                    driver2.execute_script("window.scrollTo(0,28000);")
                elif i==15:
                    driver2.execute_script("window.scrollTo(0,30000);")
                elif i==16:
                    driver2.execute_script("window.scrollTo(0,32000);")
                elif i==17:
                    driver2.execute_script("window.scrollTo(0,34000);")
                elif i==18:
                    driver2.execute_script("window.scrollTo(0,36000);")
                elif i==19:
                    driver2.execute_script("window.scrollTo(0,38000);")
                time.sleep(1)

            driver2.close()

            for drink_name, price, status, rating, store_name, address in zip(lst_drink_name, lst_prices, lst_status, lst_rating, lst_store_names, lst_address):
                item = ItemLoader(FoodyItem())
                item.add_value('drink_names', drink_name)
                item.add_value('prices', price)
                item.add_value('statuss', status)
                item.add_value('ratings', rating)
                item.add_value('store_names', store_name)
                item.add_value('address', address)
                yield item.load_item()
