import json
import requests
import pandas as pd

BASE_URL = "https://api.openweathermap.org/data/2.5/"


class OpenWeatherException(Exception):
    pass


class OpenWeather:
    def __init__(self, api_key):
        """Initialize the OpenWeather class with the API key

        Will initialize the OpenWeather class with the API key.  If the API key
        is not set, this will raise a OpenWeatherException
        """

        if api_key is None:
            raise OpenWeatherException("API key not set")

        self.api_key = api_key

    def current_weather_for_city(self, city):
        """
        Get current weather for a city

        Will return a dictionary with the current weather for a city.
        Currently does not handle API errors gracefully, so it's up to the
        calling application to detect 401s or the like.
        """

        url = f"{BASE_URL}/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return json.loads(response.text)

    def max_temp_forecast(self, city, temp):
        temp = f"{BASE_URL}/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(temp)
        return json.loads(response.text)

    def temp_interval(city, country, temperature):
        r = requests.get(
            'http://api.openweathermap.org/data/2.5/forecast?q=' + city + ',' + country + '&appid=44437e7ffa90fc0a1a7d6667fe712b8a&units=metric')
        x = r.json()

        df = pd.DataFrame(x['list'])  # creating a dataframe of the json with pandas is the only option I can think of
        df = pd.concat([df.drop(['main'], axis=1), df['main'].apply(pd.Series)], axis=1)[['dt', 'temp_max']]  # pandas
        # series to create 1d array
        count = 0
        gap_dict = {'start_dt': [], 'end_dt': [], 'count': []}  # try dictionary of lists for the dts

        for i in range(len(df)):  # loop through dataframe
            if float(df.loc[i, 'temp_max']) >= temperature:  # find max temp
                count += 1
                if count == 1:
                    gap_dict['start_dt'].append(df.loc[i, 'dt'])
            elif count == 0:
                continue
            else:
                gap_dict['end_dt'].append(df.loc[i - 1, 'dt'])  # if temp not found save end dt
                gap_dict['count'].append(count)  # store total count
                count = 0  # reset count to 0

        if len(gap_dict['start_dt']) == 0:  # if the given temp exceeds the temps at location
            df2 = str(temperature) + ' - This temperature not found at this location'

        elif len(gap_dict['start_dt']) == 1:  # if there is only 1 where temp is over max
            df2 = df[(df['dt'] >= gap_dict['start_dt'][0])]

        else:  # finding the data
            position_dt = gap_dict['count'].index(max(gap_dict['count']))
            df2 = df[(df['dt'] >= gap_dict['start_dt'][position_dt]) & (df['dt'] <= gap_dict['end_dt'][position_dt])]
            df2 = df2.reset_index().drop(['index'], axis=1)

        return df2

    city = 'Skibbereen'
    country = 'ie'
    temperature = 13.11
    result_int = temp_interval(city, country, temperature)
    result_int2 = result_int.iloc[[0, -1]]  # first and last dt
    print('Start and end dt for longest stretch of max forecast temperature over ' + str(temperature) + 'C')
    print(result_int2)
