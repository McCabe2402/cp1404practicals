import unittest
from unreliable_car import UnreliableCar


class TestUnreliableCar(unittest.TestCase):
    def test_car_drive_success(self):
        car = UnreliableCar("TestCar", 100, 100)
        car.drive(10)
        self.assertEqual(car.fuel, 90)

    def test_car_drive_fail(self):
        car = UnreliableCar("TestCar", 100, 0)
        car.drive(10)
        self.assertEqual(car.fuel, 100)

    def test_car_drive_partial(self):
        car = UnreliableCar("TestCar", 100, 50)
        car.drive(10)


if __name__ == '__main__':
    unittest.main()
