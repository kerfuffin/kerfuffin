import datetime
import matplotlib
import matplotlib.pyplot
import scipy
from copy import deepcopy
from Libs.FastMath import *

class Plot():
    def __init__(self, program):
        self.program = program
        self.connector = self.program.callback.connector
        self.canvas = self.connector.get_canvas()
        self.axes = self.canvas.figure.add_subplot(111)

        #set style
        matplotlib.pyplot.style.use("dark_background")
        self.axes.set_facecolor("#2d2d2d")
        self.axes.set_title("Air Quality", color="white")
        self.axes.set_xlabel("Time", color="white")

        self.active_plots = []
        self.active_weather_plots = []
        self.start_time_index = 0
        self.end_time_index = 0
        self.maxpoints = 100
        self.states = {}
        self.stations = []
        self.weathers = []
        self.timeline = []

        self.weather_display = {
            "temperature": "Temperatura [°C]",
            "humidity": "Wilgotność [%]",
            "wind_speed": "Prędkość wiatru [km/h]",
        }

        self.pollutants_display = {
            "PM10": "PM10 [µg/m3]",
            "NO2": "NO2 [µg/m3]",
            "CO": "CO [10 µg/m3]",

        }

    def set_timeline(self, start_date, end_date):
        self.start_time_index = self.program.data["time"].index(start_date)
        self.end_time_index = self.program.data["time"].index(end_date)
        self.timeline = self.program.data["time"][self.start_time_index : self.end_time_index]
        # datetime from string
        self.timeline = [datetime.datetime.strptime(x, "%Y-%m-%d %H:%M") for x in self.timeline]
        #self.axes.set_xticks(range(0, len(self.timeline), 1))

    def clear_station(self):
        self.active_plots = []
        self.active_weather_plots = []

    def add_station(self, station_name):
        if station_name not in self.stations:
            self.stations.append(station_name)

    def remove_station(self, station_name):
        self.stations.remove(station_name)
        self.update_all()
        # remove station from active plots

    def add_weather(self, weather):
        self.weathers.append(weather)

    def remove_weather(self, weather):
        self.weathers.remove(weather)

    def add_subplot(self, station_name, y):
        clear_data_x = []
        clear_data_y = []
        for i, e in enumerate(self.timeline):
            if self.program.data[y][station_name][i+self.start_time_index] != None:
                clear_data_x.append(e)
                if y != "CO":
                    clear_data_y.append(float(self.program.data[y][station_name][i+self.start_time_index].replace(",", ".")))
                else:
                    clear_data_y.append(float(self.program.data[y][station_name][i+self.start_time_index].replace(",", "."))*100)
        temp = self.get_average(clear_data_x, clear_data_y)
        self.active_plots.append({(station_name, y):(temp[0], temp[1])})

    def add_weather_subplot(self, weather):
        clear_data_x = []
        clear_data_y = []
        for i, e in enumerate(self.timeline):
            if self.program.weather_data[weather]["PmSopBiPlowc"][i+self.start_time_index] != None:
                clear_data_x.append(e)
                clear_data_y.append(self.program.weather_data[weather]["PmSopBiPlowc"][i+self.start_time_index])
        temp = self.get_average(clear_data_x, clear_data_y)
        self.active_weather_plots.append({(weather, weather):(temp[0], temp[1])})

    def get_average_tab(self, x):
        clear_data_x = []
        for i in range(len(x[0])):
            sum = 0
            for j in range(len(x)):
                try:
                    sum += x[j][i]
                except:
                    pass
            clear_data_x.append(sum/len(x))
        return clear_data_x
            
    def get_max_tab(self, x):
        clear_data_x = []
        for i in range(len(x[0])):
            _max = []
            for j in range(len(x)):
                try:
                    _max.append(x[j][i])
                except:
                    pass
            clear_data_x.append(max(_max))
        return clear_data_x

    def get_min_tab(self, x):
        clear_data_x = []
        for i in range(len(x[0])):
            _max = []
            for j in range(len(x)):
                try:
                    _max.append(x[j][i])
                except:
                    pass
            clear_data_x.append(min(_max))
        return clear_data_x

    def plot(self):
        self.axes.clear()
        self.axes.set_xlabel("Time")

        formatter = matplotlib.dates.ConciseDateFormatter(matplotlib.dates.AutoDateLocator())
        self.axes.xaxis.set_major_formatter(formatter)
        self.axes.xaxis.set_major_locator(matplotlib.dates.AutoDateLocator())
        
        labels = []
        #material colors for dark theme
        colors = ["#ff9800", "#4caf50", "#2196f3", "#9c27b0", "#f44336", "#ffeb3b", "#795548", "#607d8b", "#00bcd4", "#ff5722", "#8bc34a", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63", "#ff9800", "#cddc39", "#9e9e9e", "#009688", "#ff5722", "#cddc39", "#03a9f4", "#e91e63"]

        average_y = {}
        max_y = {}
        min_y = {}
        x_ticks = []
        for plot in self.active_plots:
            for key, value in plot.items():
                try:
                    average_y[key[1]].append(value[1])
                except:
                    average_y[key[1]] = [value[1]]
                    x_ticks = value[0]
        temp = deepcopy(average_y)
        for key in temp:
            average_y[key] = self.get_average_tab(temp[key])
            max_y[key] = self.get_max_tab(temp[key])
            min_y[key] = self.get_min_tab(temp[key])
        #average_y = [{"CO":[y1, y2, y3], "NO2":[y1, y2, y3], "PM10":[y1, y2, y3]}]
        qml_data = []
        if self.program.callback.connector.get_mode() != 2:
            for plot in self.active_plots:
                for key, value in plot.items():
                    _min = round(min(value[1]), 3)
                    _max = round(max(value[1]), 3)
                    _avg = round(sum(value[1])/len(value[1]), 3)
                    _amp = round(_max - _min, 3)
                    _correlation = "null"
                    for weather_plot in self.active_weather_plots:
                        for weather_key, weather_value in weather_plot.items():
                            _min_length = min(len(value[1]), len(weather_value[1]))
                            corr = scipy.stats.pearsonr(value[1][0:_min_length], weather_value[1][0:_min_length])
                            _correlation = round(corr[0], 5)
                    qml_data.append({"min": str(_min), "max": str(_max), "average": str(_avg), "amplitude": str(_amp), "correlation": str(_correlation)})
                    self.axes.plot(value[0], value[1], label=str(key[0] + " " + key[1]))
                    labels.append(str(key[0] + " " + self.pollutants_display[key[1]]))
        else:
            mode = self.program.callback.connector.get_merge_type_combo()
            k_key = None
            if mode == 0:
                k_key = average_y
            elif mode == 1:
                k_key = max_y
            elif mode == 2:
                k_key = min_y
            for key in k_key:
                min_len = min(len(x_ticks), len(k_key[key]))

                _min = round(min(k_key[key][0:min_len]), 3)
                _max = round(max(k_key[key][0:min_len]), 3)
                _avg = round(sum(k_key[key][0:min_len])/len(k_key[key][0:min_len]), 3)
                _amp = round(_max - _min, 3)
                _correlation = "null"
                for weather_plot in self.active_weather_plots:
                    for weather_key, weather_value in weather_plot.items():
                        _min_length = min(len(k_key[key][0:min_len]), len(weather_value[1]))
                        corr = scipy.stats.pearsonr(k_key[key][0:min_len][0:_min_length], weather_value[1][0:_min_length])
                        _correlation = round(corr[0], 5)
                qml_data.append({"min": str(_min), "max": str(_max), "average": str(_avg), "amplitude": str(_amp), "correlation": str(_correlation)})

                self.axes.plot(x_ticks[0:min_len], k_key[key][0:min_len], label=str(key))
                labels.append(str(self.pollutants_display[key]))
        
        for plot in self.active_weather_plots:
            for key, value in plot.items():
                _min = round(min(value[1]), 3)
                _max = round(max(value[1]), 3)
                _avg = round(sum(value[1])/len(value[1]), 3)
                _amp = round(_max - _min, 3)
                qml_data.append({"min": str(_min), "max": str(_max), "average": str(_avg), "amplitude": str(_amp), "correlation": "null"})
                self.axes.step(value[0], value[1], label=str(key[0] + " " + key[1]))
                labels.append(self.weather_display[str(key[1])])
        
        for i, e in enumerate(self.axes.get_lines()):
            print(len(qml_data))
            qml_data[i]["color"] = colors[i]
            e.set_color(colors[i])
        self.program.callback.connector.log_model_clear()
        self.program.callback.connector.log_model_append(qml_data)
        #show legend
        self.axes.legend(labels)

    def show_key(self, key):
        self.states[key.upper()] = 1

    def hide_key(self, key):
        self.temp_active_plots = []
        for plot in self.active_plots:
            if list(plot.keys())[0][1] != key.upper():
                self.temp_active_plots.append(plot)
        self.active_plots = self.temp_active_plots
    
    def get_average(self, clear_data_x, clear_data_y):
        time_diff = (self.timeline[-1] - self.timeline[0])/(3600*self.maxpoints)
        step = float(time_diff.total_seconds())
        if(step > 1):
            data_x_temp = [int(i.timestamp()) for i in clear_data_x]
            temp = gen_average(data_x_temp, clear_data_y, step)
            temp[0] = [datetime.datetime.fromtimestamp(i) for i in temp[0]]
        else:
            temp = [[] for i in range(2)]
            temp[0] = clear_data_x
            temp[1] = clear_data_y
        return temp

    def update(self, key):
        if self.states[key.upper()] == 1:
            self.show_key(key.upper())
        else:
            self.hide_key(key.upper())

    def update_all(self):
        self.clear_station()
        self.active_plots = []
        for state in self.states:
            for station_name in self.stations:
                if station_name in self.program.data[state.upper()].keys():
                    #self.program.callback.connector.set_switch_state(state, 1)
                    if self.states[state.upper()] == 1:
                        self.add_subplot(station_name, state.upper())
        for weather in self.weathers:
            self.add_weather_subplot(weather)    
