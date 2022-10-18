#!/usr/bin/python3

import os
import sys
import openweather
import requests
import pandas as pd

api_key = os.environ.get("44437e7ffa90fc0a1a7d6667fe712b8a", None)
loc_list = ['Skibbereen,ie', 'Dublin,ie', 'Paris,fr']  # list of locations for the coldest location function

try:
    ow = openweather.OpenWeather("44437e7ffa90fc0a1a7d6667fe712b8a")
except openweather.OpenWeatherException:
    print("You must set the environmental variable OPENWEATHER_API_KEY")
    sys.exit(1)

data = ow.current_weather_for_city("Skibbereen,ie")

location = data["name"]
temp = data['main']['temp_max']
weather = data["weather"][0]
print(f"{location}: {weather['main']} - {weather['description']}")


def coldest_location(locations_list, self=None):  # using pandas to create a dataframe again
    df_list = []

    for i in loc_list:  # looping through the list of locations
        city, country = i.split(',')
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/forecast?q=' + city + ',' + country + '&appid=44437e7ffa90fc0a1a7d6667fe712b8a&units=metric')
        x = r.json()
        df = pd.DataFrame(x['list'])
        df = pd.concat([df.drop(['main'], axis=1), df['main'].apply(pd.Series)], axis=1)[['dt', 'temp_min']]
        df['city'] = city
        df_list.append(df)

    df_all = pd.concat(df_list)
    df_all = df_all.reset_index().drop(['index'], axis=1)
    result1 = df_all.iloc[df_all['temp_min'].idxmin()]  # finding the min temp

    return result1['dt'], result1['temp_min'], result1['city']  # return results


dt, temp, city = coldest_location(loc_list)
print('Coldest location is: ' + city + ' with temperature ' + str(temp) + 'C at timestamp ' + str(dt))

"""
ow1 = openweather.OpenWeather(api_key)
data1 = ow1.max_temp_forecast("Dublin, ie")
location1 = data1["name"]
temp1 = data1['main']['temp_max']
for temperatures in data1:
    print(temp1)
"""
