import datetime

today = datetime.date.today()
future = datetime.date(2036,4,21)
diff = future - today

days_left = (diff.days)
print(days_left)
