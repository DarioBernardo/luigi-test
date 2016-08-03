import os
from datetime import date, datetime

import pandas as pd
from Temperature_data_generator import generate_data_for
from beans.Place import Place
from settings_loader import DATA_FOLDER

dataset_list = Place.get_all_places()[:1]

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