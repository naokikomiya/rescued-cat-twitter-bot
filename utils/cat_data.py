import os
import random
from urllib import request

from selenium import webdriver

from utils import driver_option


def get(url, xpath1, xpath2):
    # heroku上のdriverパス
    # '/app/.chromedriver/bin/chromedriver'
    options = driver_option.get()
    chrome_driver_path = os.environ.get('CHROME_DRIVER_PATH')
    driver = webdriver.Chrome(
        options=options, executable_path=chrome_driver_path)

    wait_time = 5
    # 一度設定すればOK
    driver.implicitly_wait(wait_time)

    # URLを開く
    all_cats_url = url
    driver.get(all_cats_url)

    # ページ内のネコリンクを配列で取得
    cats_link_list = driver.find_elements_by_xpath(
        xpath1)

    # ページ内に表示されているネコの数
    cats_link_length = len(cats_link_list)
    # ネコ数内で乱数生成
    random_number = random.randint(0, (cats_link_length - 1))
    # ランダムに１ネコ選びリンク先へ遷移
    cats_link_list[random_number].click()
    # 詳細ページのURLを取得(ツイート文言に入れるためreturnする)
    cat_page_url = driver.current_url

    # 詳細ページの大きい画像要素を取得
    cat_img = driver.find_element_by_xpath(
        xpath2)
    # 画像URL
    img_url = cat_img.get_attribute('src')
    # プロジェクトルートに保存
    request.urlretrieve(img_url, 'cat.png')

    print(cat_page_url)
    return cat_page_url
