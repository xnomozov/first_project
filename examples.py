from abc import ABC, abstractmethod
from typing import Union


# abstraction
class Shape(ABC):
    @abstractmethod
    def area(self) -> None:
        pass


class Rectangle(Shape):
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y

    def area(self) -> Union[int, float]:
        """This method calculates the area of a rectangle and return it"""
        return self.x * self.y


r = Rectangle(10, 20)
print('area: ', r.area())


# Inheritance
class Vehicle:
    def __init__(self, name: str, speed: int) -> None:
        self.name = name
        self.speed = speed

    def drive(self) -> None:
        """This method print driving car name"""
        print(f"Driving {self.name}")


class Car(Vehicle):
    def __init__(self, name: str, speed: int, mileage: int) -> None:
        super().__init__(name, speed)
        self.mileage = mileage


car = Car("BMW", 120, 10)
print(car.name, car.speed, car.mileage)
car.drive()


# Polymorphism
class Country:
    def capital(self) -> None:
        pass

    def language(self) -> None:
        pass

    def type(self) -> None:
        pass


class India(Country):
    def capital(self) -> None:
        """ This method prints capital of country"""
        print("New Delhi is the capital of India.")

    def language(self) -> None:
        """ This method prints language of country"""
        print("Hindi is the most widely spoken language of India.")

    def type(self) -> None:
        """ This method prints type of country"""
        print("India is a developing country.")


class USA(Country):
    def capital(self) -> None:
        """ This method prints capital of country"""
        print("Washington, D.C. is the capital of USA.")

    def language(self) -> None:
        """ This method prints language of country"""
        print("English is the primary language of USA.")

    def type(self) -> None:
        """ This method prints type of country"""
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()


# Encapsulation

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        """This method returns name of person"""
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """This method sets name of person"""
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise ValueError("Name must be a string")

    @property
    def age(self) -> int:
        """This method returns age of person"""
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        """This method sets age of person"""
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            raise ValueError("Age must be a non-negative integer")
