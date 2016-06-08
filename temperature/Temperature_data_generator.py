import logging

import pandas as pd

from temperature.functions.QueryGenerator import generate_query
from temperature.webapi.Interrogator import Interrogator

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
# logging.basicConfig(filename='temperature_app.log', level=logging.INFO)

def get_temperature_history_for_location(starting_year, starting_month, starting_day, state, city):

    query_list = generate_query(starting_year, starting_month, starting_day, state, city)

    temperature_history = []
    for request_number, query in enumerate(query_list):
        interrogator = Interrogator()
        temp_temperature = interrogator.execute(query)
        temperature_history.append(temp_temperature)

        if ((request_number+1) % 10) == 0:
            logging.info("Number of requests executed for {} is: {}".format(city, request_number))

    return temperature_history

def translate_temperature_list_into_dataframe(list):

    min = []
    max = []
    dates = []

    for temperature in list:
        # print(temperature)
        min.append(temperature.temperature_min)
        max.append(temperature.temperature_max)
        dates.append(temperature.date)

    dict = {'date':dates, 'min_temperature':min, 'max_temperature':max}
    return pd.DataFrame(dict)



def generate_data_for(year, month, day, state, city):
    history_for_location = get_temperature_history_for_location(int(year), int(month), int(day), state, city)
    df = translate_temperature_list_into_dataframe(history_for_location)
    return df


if __name__ == "__main__":

    year = "2015"
    month = "03"
    day = "01"
    #state = "CA"
    # state = "uk"
    # state = "italy"
    state = "sweden"
    #city="San_Francisco"
    # city="london"
    # city="rome"
    city="stockholm"

    df = generate_data_for(year, month, day, state, city)
    df.to_csv("{}_temperature.csv".format(city), sep=',', encoding='utf-8', index=False)