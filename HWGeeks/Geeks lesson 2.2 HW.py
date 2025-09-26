# Родительский класс
class Transport:
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    def info(self):
        return f"{self.name}: скорость {self.speed} км/ч, вместимость {self.capacity}"

    def move(self):
        return f"{self.name} движется со скоростью {self.speed} км/ч"



class Car(Transport):
    def __init__(self, name, speed, capacity, fuel_type):
        super().__init__(name, speed, capacity)
        self.fuel_type = fuel_type


    def move(self):
        return f"Автомобиль {self.name} едет по дороге со скоростью {self.speed} км/ч. Топливо: {self.fuel_type}"



t = Transport("Катер", 40, 10)
print(t.info())
print(t.move())

c = Car("Toyota", 120, 5, "бензин")
print(c.info())
print(c.move())
