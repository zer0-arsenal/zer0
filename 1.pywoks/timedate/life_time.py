import datetime

today = datetime.date.today()
birthday = datetime.date(1994,8,19)

life = today - birthday

print(life.days)
