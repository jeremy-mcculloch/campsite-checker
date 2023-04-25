from apscheduler.schedulers.background import BackgroundScheduler
from camping import main_permits
from utils.camping_argparser import CampingArgumentParser
import time

def test_job():
    main_permits(
        [72192], #when you search for permits the url should be https://www.recreation.gov/permits/[#####], replace 72192 with the number at the end 
        CampingArgumentParser.TypeConverter.date("2023-05-05"), #First date that you are interested in permits for
        CampingArgumentParser.TypeConverter.date("2023-05-06") # Last date that you are interested in permits for (make same as start date if only interested in one day)
    )

scheduler = BackgroundScheduler()
job = scheduler.add_job(test_job, 'interval', minutes=10) #How frequently to query 
scheduler.start()

while True:
    time.sleep(1)
