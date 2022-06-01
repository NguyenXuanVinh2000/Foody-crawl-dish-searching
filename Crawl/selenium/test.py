from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/vinh/PROJECT CTY/Dish_Searching/Crawl/selenium/chromedriver_linux64/chromedriver")

url = "https://www.foody.vn/da-nang"
driver.get(url)
time.sleep(3)
link = driver.find_element_by_xpath('//*[@id="box-delivery"]/div[1]/div[2]/ul/li[4]/a')
link.click()
time.sleep(3)

urls_stores = []

    
for store in driver.find_elements_by_css_selector('li[ng-repeat="item in ListItems.Items"]'):
    el = store.find_element_by_css_selector('a[class="avatar"]')
    link_store = el.get_attribute('href')
    print(link_store)
    urls_stores.append(link_store)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[2]/i[1]').click()
time.sleep(3)

for i in range(0, 99):
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[2]/i[2]').click()
    time.sleep(3)
    for store in driver.find_elements_by_css_selector('li[ng-repeat="item in ListItems.Items"]'):
        el = store.find_element_by_css_selector('a[class="avatar"]')
        link_store = el.get_attribute('href')
        print(link_store)
        urls_stores.append(link_store)

urls_stores = set(urls_stores)
urls_stores = list(urls_stores)
with open(r'/home/vinh/PROJECT CTY/Dish_Searching/Crawl/selenium/store.txt', 'w') as fp:
    for item in urls_stores:
        fp.write("%s\n" % item)
    print('Done')
