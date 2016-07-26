import json
from datetime import datetime

from src.beans.Temperature import Temperature


class JsonTemperatureParser:

    def __init__(self, json_string, city):
        self.parsed_json = json.loads(json_string)
        self.measurement_city = city
        if "error" in self.parsed_json['response']:
            error = self.parsed_json['response']['error']
            raise Exception("API REQUEST ERROR: {}".format(error))

    def marsh_object(self):
        daily_summary = self.parsed_json["history"]["dailysummary"][0]

        json_date = datetime(year=int(daily_summary['date']['year']), month=int(daily_summary['date']['mon']),
                                     day=int(daily_summary['date']['mday']), hour=int(daily_summary['date']['hour']),
                                     minute=int(daily_summary['date']['min']))

        return Temperature(self.measurement_city, daily_summary['mintempm'], daily_summary['maxtempm'], json_date)

    def save_json_on_disk(self, json_string):
        print("not implemented yet!")