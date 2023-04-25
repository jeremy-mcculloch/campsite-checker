from apscheduler.schedulers.background import BackgroundScheduler
from camping import main_permits
from utils.camping_argparser import CampingArgumentParser
import time

def test_job():
    main_permits([72192], CampingArgumentParser.TypeConverter.date("2023-05-05"), CampingArgumentParser.TypeConverter.date("2023-05-06"))

scheduler = BackgroundScheduler()
job = scheduler.add_job(test_job, 'interval', minutes=10)
scheduler.start()

while True:
    time.sleep(1)
