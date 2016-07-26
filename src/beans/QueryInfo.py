

class QueryInfo:

    def __init__(self, year, month, day, state, city):
        self.state = state
        self.city = city
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "Query for {day:02d}/{month:02d}/{year} location: {city} ({state})".format(
            day=self.day, month=self.month, year=self.year, city=self.city, state=self.state)