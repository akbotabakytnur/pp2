from datetime import datetime,timedelta
today=datetime.now()
newd=today - timedelta(days=5)
yest=today - timedelta(days=1)
tomr=today + timedelta(days=1)
without_microseconds = today.replace(microsecond=0)
difference=tomr-newd
seconds=difference.total_seconds()
#1
print("5 days ago: ",newd)
#2
print(today)
print(yest)
print(tomr)
#3
print(without_microseconds)
#4
print(seconds)

