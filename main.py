from apscheduler.schedulers.blocking import BlockingScheduler

from utils import tweet


def main():
    tweet.post()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # scheduler.add_job(main, 'interval', minutes=10)
    scheduler.add_job(main, 'cron', hour='1', minute='45')
    scheduler.start()
