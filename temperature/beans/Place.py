class Place:
    def __init__(self, state, city):
        self.state = state
        self.city = city

    def get_filename(self):
        return "{}_temperature.csv".format(self.city)

    @staticmethod
    def get_all_places():
        dataset_list = [Place('italy', 'rome'), Place('italy', 'terme'), Place('uk', 'london'),
                        Place('sweden', 'stockholm')]
        return dataset_list
