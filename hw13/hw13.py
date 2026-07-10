from datetime import datetime

class Car:
    number_of_cars = 0 #მანქანების რაოდენობა

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.number_of_cars += 1

    def age_of_car(self):
        return datetime.now().year - self.year #ახლანდელ წელს აკლებს გამოშვების წელს
    
    def car_info(self):
        print(f"ბრენდი: {self.brand}")
        print(f"მოდელი: {self.model}")
        print(f"წელი: {self.year}")
        print(f"მანქანის ასაკი: {self.age_of_car()}")

    @classmethod
    def total_cars(cls):
         print(f"მანქანების რაოდენობა: {cls.number_of_cars}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battary_life):
        super().__init__(brand, model,year)
        self.battary_life = battary_life

    def battery_info(self):
        print(f"ელემენტის ხანგძლივობა შეადგენს {self.battary_life} საათს")


