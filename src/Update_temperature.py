import os

print(os.path)


from datetime import date, datetime

from settings import DATA_FOLDER
from src.Temperature_data_generator import generate_data_for
from src.beans.Place import Place
import pandas as pd

dataset_list = Place.get_all_places()

for place in dataset_list:
    print("Updating {}".format(place.get_filename()))

    df = pd.read_csv(os.path.join(DATA_FOLDER, place.get_filename()), sep=',', parse_dates=[0], encoding='utf-8')
    date_max = df.date.max()

    starting_date = date_max + pd.DateOffset(days=1)

    print("Last temperature was collected at {} starting at {}".format(date_max, starting_date))

    today = date(datetime.today().year, datetime.today().month, datetime.today().day)

    if starting_date.year != today.year or starting_date.month != today.month or starting_date.day != today.day:
        df_new = generate_data_for(starting_date.year, starting_date.month, starting_date.day, place.state, place.city)
        print("New Data:")
        print(df_new)

        df = df.append(df_new, ignore_index=True)
        df.to_csv(os.path.join(DATA_FOLDER, place.get_filename()), sep=',', encoding='utf-8', index=False)
    else:
        print("Data is already updated!")