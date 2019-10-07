from selenium.webdriver.chrome.options import Options


def option():
    # ブラウザ起動オプション
    options = Options()
    # ヘッドレスブラウザで実行
    options.add_argument('--headless')
    # 画面サイズにより要素のxpathが変わる事があるのでサイズを決めておく
    options.add_argument('--window-size=1980,1080')
    # キャッシュを使わない  削除したはずの要素が残る場合がある
    options.add_argument("--disable-application-cache")
    return options
