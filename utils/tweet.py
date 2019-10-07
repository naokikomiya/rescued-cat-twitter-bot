import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests_oauthlib import OAuth1Session

from . import cat_data
from config import settings


def post():
    end_point_media = "https://upload.twitter.com/1.1/media/upload.json"
    end_point_text = "https://api.twitter.com/1.1/statuses/update.json"
    image_path = './cat.png'
    cat_page_url = cat_data.get()
    message = f'\n✦里親を募集しています \n\n {cat_page_url} \n\n#拡散\n#してくれると\n#うれしい\n#けど'

    # OAuth認証 セッションを開始
    twitter = OAuth1Session(settings.CONSUMER_KEY,
                            settings.CONSUMER_SECRET,
                            settings.ACCESS_TOKEN,
                            settings.ACCESS_TOKEN_SECRET)

    # 画像投稿
    files = {"media": open(image_path, 'rb')}
    req_media = twitter.post(end_point_media, files=files)

    # レスポンスを確認
    if req_media.status_code == 200:
        print("画像アップデート成功: %s", req_media.text)
    else:
        print("画像アップデート失敗: %s", req_media.text)
        exit()

    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    print("Media ID: %d" % media_id)

    # Media ID を付加してテキストを投稿
    params = {'status': message, "media_ids": [media_id]}
    req_text = twitter.post(end_point_text, params=params)

    # 再びレスポンスを確認
    if req_text.status_code == 200:
        print("テキストアップデート成功: %s", req_text.text)
    else:
        print("テキストアップデート失敗: %s", req_text.text)
        exit()

    print("Done")
