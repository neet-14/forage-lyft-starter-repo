import unittest
from datetime import datetime

from car_factory import CarFactory


class TestCarFactory(unittest.TestCase):
    def test_calliope(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(today,last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_rorschach(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())