from apscheduler.schedulers.blocking import BlockingScheduler

from utils import tweet


def main():
    tweet.post()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # scheduler.add_job(main, 'interval', minutes=10)
    japan_hour = 18
    utc = japan_hour - 9
    scheduler.add_job(main, 'cron', hour=str(utc))
    scheduler.start()
