from urllib.request import urlopen

from json_temperature.JsonTemperatureParser import JsonTemperatureParser

import settings_loader as settings


class Interrogator:

    def __init__(self):
        with open(settings.WEBSERVER_KEY) as f:
            self.key = f.readline()

    def execute(self, query):

        f = urlopen('http://api.wunderground.com/api/{key}/history_{year}{month:02d}{day:02d}/q/{state}/{city}.json'
                    .format(year=query.year, month=query.month, day=query.day,
                            state=query.state, city=query.city, key=self.key))

        json_string = f.read().decode('utf-8')
        f.close()

        temperature_parser = JsonTemperatureParser(json_string, query.city)
        temperature = temperature_parser.marsh_object()
        return temperature
