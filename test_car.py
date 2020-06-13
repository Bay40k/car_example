import unittest

import car
from car import make_car_lot


class TestCarMethods(unittest.TestCase):

    # Test data
    car_data = [
        {
            "make": "Mitsubishi",
            "model": "Evo V",
            "year": "1999"
        },
        {
            "make": "Subaru",
            "model": "BRZ",
            "year": "2016"
        }
    ]

    def test_make_car_lot(self) -> list:
        car_data = self.car_data

        car_lot = make_car_lot(car_data)
        self.assertEqual(type(car_lot), list)

        for i, c in enumerate(car_lot):
            # print(f"{car.id}. {car.name_string}")

            self.assertEqual(c.id, i)

            # Make sure objects match data
            if i == 1:
                self.assertEqual(c.make, "Subaru")
                self.assertEqual(c.model, "BRZ")
                self.assertEqual(c.year, "2016")

        return car_lot

    def test_turbo(self):
        car_lot = self.test_make_car_lot()
        for c in car_lot:
            # WIP
            # self.assertEqual(c.turbo, False)
            pass

if __name__ == '__main__':
    unittest.main()
