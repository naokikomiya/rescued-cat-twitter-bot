import random
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utils import web_driver


def get():
    url = 'https://tokyocatguardian.org/cats_date/'
    wait_time = 5

    driver_path = '/app/.chromedriver/bin/chromedriver'
    options = web_driver.option()
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get(url)

    driver.implicitly_wait(wait_time)
    child_cats_list = driver.find_elements_by_xpath(
        '/html/body/div[1]/div/div[2]/div/article[1]/div[2]/div/div/a')

    child_cats_length = len(child_cats_list)
    random_number = random.randint(0, (child_cats_length - 1))

    cat_page_url = child_cats_list[random_number].get_attribute('href')
    child_cats_list[random_number].click()

    driver.implicitly_wait(wait_time)
    cat_img = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/section/section[1]/img')
    img_url = cat_img.get_attribute('src')
    urllib.request.urlretrieve(img_url, 'cat.png')

    print(cat_page_url)
    return cat_page_url
