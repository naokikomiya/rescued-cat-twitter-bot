from selenium.webdriver.chrome.options import Options


def get():
    # ブラウザ起動オプション
    options = Options()
    # ヘッドレスブラウザで実行
    options.add_argument('--headless')
    # gpuを使わない
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    # ヘッドレスブラウザのパフォーマンスアップ
    options.add_argument('--proxy-server="direct://"')
    options.add_argument('--proxy-bypass-list=*')
    # 画面サイズにより要素のxpathが変わる事があるのでサイズを決めておく
    # options.add_argument('--window-size=1980,1080')
    options.add_argument('--start-maximized')
    # キャッシュを使わない  削除したはずの要素が残る場合がある
    options.add_argument('--disable-application-cache')
    # binary path を指定
    return options
