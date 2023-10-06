"""
HW13_3

В организации есть два типа людей: сотрудники и обычные люди.

Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая)
Имя (строка, не пустая)
Отчество (строка, не пустая)
Возраст (целое положительное число)

Сотрудники имеют также
уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для
управления данными о людях (Фамилия, Имя, Отчество, Возраст).

Класс должен проверять валидность входных данных и генерировать
исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person
и добавлять уникальный идентификационный номер (ID).

Класс Employee также должен проверять валидность ID
и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee,
который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными
и проверить, что исключения работают корректно при передаче неверных данных.
"""
class InvalidNameError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not isinstance(self.value, str):
            return f'Invalid name: {self.value}. Name should be a string.'
        elif len(self.value) < 1:
            return f'Invalid name: {self.value}. Name should be a non-empty string.'


class InvalidAgeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not isinstance(self.value, int):
            return f'Invalid age: {self.value}. Age should be an integer.'
        elif self.value <= 0:
            return f'Invalid age: {self.value}. Age should be a positive integer.'

class InvalidIdError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if not isinstance(self.value, int):
            return f'Invalid id: {self.value}. Id should be an integer.'
        elif not (100000 <= self.value <= 999999):
            return f'Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999.'

class Person:

    def __init__(self, last_name: str, first_name: str, second_name: str, age: int):
        if not isinstance(last_name, str) or len(last_name) < 1:
            raise InvalidNameError(last_name)
        elif not isinstance(first_name, str) or len(first_name) < 1:
            raise InvalidNameError(first_name)
        elif not isinstance(second_name, str) or len(second_name) < 1:
            raise InvalidNameError(second_name)
        elif not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)
        self.last_name = last_name
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, second_name: str, age: int, _id: int):
        super().__init__(last_name, first_name, second_name, age)
        if not isinstance(_id, int) or not (100000 <= _id <= 999999):
            raise InvalidIdError(_id)
        self._id = _id

    @property
    def get_level (self):
        return self._id % 7

person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())