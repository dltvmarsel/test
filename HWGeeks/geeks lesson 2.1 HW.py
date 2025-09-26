class Car:
    def __init__(self, model, speed, fuel):
        self.model = model
        self.speed = speed
        self.fuel = fuel

    def drive(self, distance):
        if self.fuel <= 0:
            return f"{self.model} не может ехать — нет топлива!"
        else:
            fuel_used = distance * 0.1
            if fuel_used > self.fuel:
                return f"{self.model} проехал только {self.fuel / 0.1:.1f} км и заглох — топливо кончилось."
            else:
                self.fuel -= fuel_used
                return f"{self.model} проехал {distance} км. Осталось топлива: {self.fuel:.1f} л."


car1 = Car("Toyota", 180, 20)
car2 = Car("BMW", 220, 5)

print(car1.drive(100))
print(car2.drive(80))
