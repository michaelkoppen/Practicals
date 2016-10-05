class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 2016-year

    def get_age(self):
        return "{}".format(self.age)

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)
