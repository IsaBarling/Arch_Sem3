'''
Принцип разделения интерфейса (ISP):

Созданы разные интерфейсы для каждой операции, чтобы не заставлять классы реализовывать методы, 
которые им не нужны.
Принцип инверсии зависимостей (DIP):

Высокоуровневые модули (например, панель управления автомобилем) будут зависеть от абстракций, 
а не от конкретных реализаций компонентов.

'''

from abc import ABC, abstractmethod

# Принцип разделения интерфейса (ISP)
class IEngine(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class IRadio(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass


class IAirConditioner(ABC):
    @abstractmethod
    def activate(self):
        pass
    
    @abstractmethod
    def deactivate(self):
        pass


# Реализации компонентов
class Engine(IEngine):
    def start(self):
        print("Engine started")
    
    def stop(self):
        print("Engine stopped")


class Radio(IRadio):
    def turn_on(self):
        print("Radio turned on")
    
    def turn_off(self):
        print("Radio turned off")


class AirConditioner(IAirConditioner):
    def activate(self):
        print("Air conditioner activated")
    
    def deactivate(self):
        print("Air conditioner deactivated")


# Панель управления, демонстрирующая принцип инверсии зависимостей (DIP)
class CarControlPanel:
    def __init__(self, engine: IEngine, radio: IRadio, air_conditioner: IAirConditioner):
        self.engine = engine
        self.radio = radio
        self.air_conditioner = air_conditioner
        
    def start_car(self):
        self.engine.start()
        self.radio.turn_on()
        self.air_conditioner.activate()
        
    def stop_car(self):
        self.engine.stop()
        self.radio.turn_off()
        self.air_conditioner.deactivate()


# Демонстрация
car = CarControlPanel(Engine(), Radio(), AirConditioner())
car.start_car()
print("---")
car.stop_car()
