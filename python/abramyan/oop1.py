class Car:
    color = ""
    vendor = ""
    speedometer = 0
    def __init__(self,color,vendor,speedometer):
        self.color = color
        self.vendor = vendor
        self.speedometer = speedometer
    def __str__(self):
        return f"Vendor: {self.vendor}, color: {self.color}, km: {self.speedometer}"
    def move(self,km):
        self.speedometer += km

moshin = Car("white","BMW",100)
moshin.move(18000)
print(moshin)

class Truck(Car):
    wheels = 4
    def __init__(self,wheels,vendor,color,speedometer):
        super().__init__(color,vendor,speedometer)
        self.wheels = wheels

gruzovik = Truck(8,"Mersedess","black",5000)
print(gruzovik)
print("wheels:",gruzovik.wheels)