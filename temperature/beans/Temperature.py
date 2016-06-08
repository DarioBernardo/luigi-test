class Temperature:

    def __init__(self, location, temp_min, temp_max, date):
        self.location = location
        self.temperature_min = temp_min
        self.temperature_max = temp_max
        self.date = date

    def __str__(self):
        return "Average temperature in {place}, at {time} is: max={max} C / min={min} C".format(
            place=self.location, time=self.date, max=self.temperature_max, min=self.temperature_min)
