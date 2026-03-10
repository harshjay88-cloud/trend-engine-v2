import schedule
import time
from collectors.youtube_suggest import get_suggestions

def collect():

    data = get_suggestions("music")

    print(data)

schedule.every(2).hours.do(collect)

while True:

    schedule.run_pending()

    time.sleep(60)
