class Turbo(object):
    def __init__(self):
        self.turbo = False

class Car(Turbo):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.name_string = f"{self.year} {self.make} {self.model}"


def make_car_lot(raw_cars_data: list) -> list:
    """
    Creates and returns a list of Car objects

    Takes list of dict objects as input
    """

    car_objects = []

    for i, car in enumerate(raw_cars_data):
        make = car["make"]
        model = car["model"]
        year = car["year"]
        new_car = Car(make, model, year)
        new_car.id = i
        car_objects.append(new_car)

    return car_objects
