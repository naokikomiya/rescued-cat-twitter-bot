from apscheduler.schedulers.blocking import BlockingScheduler

from utils import tweet


def main():
    def tweet_tokyo_cat_gardian():
        tweet.post(url='https://tokyocatguardian.org/cats_date/',
                   xpath1='/html/body/div[1]/div/div[2]/div/article[1]/div[2]/div/div/a',
                   xpath2='/html/body/div[1]/div/div/div/section/section[1]/img',
                   xpath3=None)

    def tweet_satooya_boshu():
        tweet.post(url='https://satoya-boshu.net/foster/?@button_name@=search&FosterParent_CategoryID=1',
                   xpath1='/html/body/main/div/div[3]/div[2]/ul[2]/li',
                   xpath2='//*[@id="slider"]/div[1]/div[1]/div/div[1]/div/img',
                   xpath3='/html/body/main/div/div[3]/ul/li[1]/h2')

    scheduler = BlockingScheduler()
    japan_hour = 18
    utc = japan_hour - 9
    scheduler.add_job(tweet_tokyo_cat_gardian,
                      'interval',
                      start_date=f"2019-10-10 {utc}:00:00",
                      days=2)
    scheduler.add_job(tweet_satooya_boshu,
                      'interval',
                      start_date=f"2019-10-11 {utc}:00:00",
                      days=2)
    # scheduler.add_job(main, 'interval', seconds=5)
    scheduler.start()
    print('start scheduler')


if __name__ == '__main__':
    main()
