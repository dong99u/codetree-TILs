import datetime as dt

class Weather:
    def __init__(self, date, day, weather):
        self.date = dt.datetime.strptime(date, '%Y-%m-%d').date()
        self.day = day
        self.weather = weather

n = int(input())

informations = [
    Weather(date, day, weather) for (date, day, weather) in (input().split() for _ in range(n))
    if weather == 'Rain'
]

informations.sort(key=lambda elem: elem.date)

x = informations[0]
print(f'{x.date} {x.day} {x.weather}')