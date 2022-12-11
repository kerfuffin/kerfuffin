import datetime
import json
import numpy as np
from meteostat import Point, Hourly, Daily

class Weather:
    def __init__(self, city, date_start, date_end):
        self.city = city
        self.date = date_start
        self.date_end = date_end
        self.weather = self.get_weather()

    def get_weather(self):
        point = Point(np.float32(self.city['lat']), np.float32(self.city['lon']))
        weather = Hourly(point, self.date, self.date_end)
        weather = weather.fetch()
        return weather

    def get_time(self):
        timestamps = len(self.weather.iloc[:, 0].values)
        dates = []
        for i in range(timestamps):
            dates.append(self.date + datetime.timedelta(hours=i))
        return_dates = []
        for date in dates:
            return_dates.append(date.strftime("%Y-%m-%d %H:%M:%S"))
        return return_dates

    def get_temperature(self):
        return self.weather['temp'].values

    def get_humidity(self):
        return self.weather['rhum'].values

    def get_wind_speed(self):
        return self.weather['wspd'].values

# load stations
with open("stacje3.json", "r") as f:
    stations = json.load(f)

for station in stations:
    city = station["city"]
    date_start = datetime.datetime(2020, 1, 1)
    date_end = datetime.datetime(2020, 1, 2)

    weather = Weather(station, date_start, date_end)
    print(station["name"], city)
    print(weather.get_time(), weather.get_temperature(), weather.get_humidity(), weather.get_wind_speed(), sep="\n")
