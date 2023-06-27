from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour

result = datetime.ctime(simdi)
result = datetime.strftime(simdi, '%Y') #Text customize
result = datetime.strftime(simdi, '%X')
result = datetime.strftime(simdi, '%A')
result = datetime.strftime(simdi, '%X %A %B %C') #datetime python format

t = '27 June 2023 Hour: 20:48:12'
result = datetime.strptime(t, '%d %B %Y Hour: %H:%M:%S')
result = result.year

birthday = datetime(1990, 5, 5, 12, 30, 10)

result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result)
result = datetime.fromtimestamp(0)

# result = simdi - birthday
# result = result.seconds
# result = result.days

print(simdi)
#result = simdi + timedelta(days=10)
result = simdi + timedelta(days=20, minutes=10)
#result = simdi - timedelta(days=10)


print(result)

