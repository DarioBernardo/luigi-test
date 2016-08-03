import logging
import os

import pandas as pd
from functions.QueryGenerator import generate_query
from settings_loader import DATA_FOLDER
from webapi.Interrogator import Interrogator
from tqdm import tqdm

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
# logging.basicConfig(filename='temperature_app.log', level=logging.INFO)

def get_temperature_history_for_location(starting_year, starting_month, starting_day, state, city):

    query_list = generate_query(starting_year, starting_month, starting_day, state, city)

    logging.info("Getting data for {}:".format(city))
    temperature_history = []
    for query in tqdm(query_list):
        interrogator = Interrogator()
        temp_temperature = interrogator.execute(query)
        temperature_history.append(temp_temperature)

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
    df.to_csv(os.path.join(DATA_FOLDER, "{}_temperature.csv".format(city)), sep=',', encoding='utf-8', index=False)