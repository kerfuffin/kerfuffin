import requests
import pandas as pd
import json
from geopy.geocoders import Nominatim
from random import randint
# plik = "stacje.csv"

# #read 6-th row from csv file
# df = pd.read_csv(plik, sep=';', header=None, skiprows=1, nrows=1)
# #convert to list
# df = df.values.tolist()[0][0].split(',')[1:]

# url = "https://powietrze.gios.gov.pl/pjp/current/station_details/info/"

# stations = []

# for i in range(2000):
#     try:
#         r = requests.get(url+str(i))
#         if r.status_code == 200:
#             if "Adres" in r.text:
#                 name = r.text.split("<th>Kod krajowy</th>")[1].split("<td>")[1].split("</td>")[0].strip()
#                 lat = r.text.split("&Phi;")[1].split(" <br/>")[0].strip()
#                 lon = r.text.split("&lambda;")[1].split(" </td>")[0].strip()
#                 print(name, lat, lon)
#                 if name in df:
#                     stations.append({"name": name, "lat": lat, "lon": lon})

#     except:
#         pass

# print(json.dumps(stations, indent=4, ensure_ascii=False))


def get_city_from_coords(station):
    lat, lon = station["lat"], station["lon"]
    print("Getting city from coords", lat, lon)
    geolocator = Nominatim(user_agent="XD" * randint(1,40))
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.raw['address']

    
with open("stacje2.json", "r") as f:
    stations = json.load(f)
    clear_stations = []
    for station in stations:
        city = get_city_from_coords(station)
        try:
            if city['city'] in ["Gdańsk", "Sopot", "Gdynia"]:
                print("Found city", city['city'])
                station["city"] = city['city']
                clear_stations.append(station)
        except:
            pass

with open("stacje3.json", "w") as f:
    f.write(json.dumps(clear_stations, indent=4, ensure_ascii=False))

    
        