from datetime import datetime

from dateutil.relativedelta import relativedelta

start_date = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
end_date = datetime(2023, 7, 26, 1, 21, 20)
print(date < end_date)

