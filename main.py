from apscheduler.schedulers.blocking import BlockingScheduler

from utils import tweet


def main():
    tweet.post()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', seconds=10)
    scheduler.start()
