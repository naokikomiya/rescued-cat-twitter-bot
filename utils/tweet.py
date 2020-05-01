import json

from requests_oauthlib import OAuth1Session

from . import cat_data
from config import settings


def post(url, xpath1, xpath2, xpath3):
    """ TwitterAPIをつかいツイートする。

    Parameter
    ---------
    xpath1, xpath2, xpath3 : str
        取得要素へ到達するまでのxpath
        cat_data.pyのget()メソッドへわたす
    """
    end_point_media = 'https://upload.twitter.com/1.1/media/upload.json'
    end_point_text = 'https://api.twitter.com/1.1/statuses/update.json'
    image_path = './cat.png'

    # このタイミングで画像もダウンロードされる
    cat_data_dict = cat_data.get(url, xpath1, xpath2, xpath3)
    cat_page_url = cat_data_dict['url']
    page_title = ''
    if xpath3:
        page_title = f'✦ {cat_data_dict['title']} ✦'

    # Tweetメッセージ
    message = f'ネコです。\n#里親募集 してます。\n\n●掲載タイミングの関係等で既に譲渡されていたり体調によって譲渡対象から外れている場合があります\n●里親お申し込み方法は各ページを参照してください\n\n{cat_page_url}\n\n{page_title}'

    # OAuth認証 セッションを開始
    twitter = OAuth1Session(settings.CONSUMER_KEY,
                            settings.CONSUMER_SECRET,
                            settings.ACCESS_TOKEN,
                            settings.ACCESS_TOKEN_SECRET)

    # 画像投稿
    files = {'media': open(image_path, 'rb')}
    req_media = twitter.post(end_point_media, files=files)

    # レスポンスを確認
    if req_media.status_code == 200:
        print('画像アップデート成功: %s', req_media.text)
    else:
        print('画像アップデート失敗: %s', req_media.text)
        exit()

    # Media ID を取得
    media_id = json.loads(req_media.text)['media_id']
    print('Media ID: %d' % media_id)

    # Media ID を付加してテキストを投稿
    params = {'status': message, 'media_ids': [media_id]}
    req_text = twitter.post(end_point_text, params=params)

    # 再びレスポンスを確認
    if req_text.status_code == 200:
        print('テキストアップデート成功: %s', req_text.text)
    else:
        print('テキストアップデート失敗: %s', req_text.text)
        exit()

    print('Done')
