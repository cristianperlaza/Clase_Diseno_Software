from abc import ABC, abstractmethod


class interruptor(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Bombilla(interruptor):
    def turn_on(self):
        print("Bombilla: turned on...")

    def turn_off(self):
        print("Bombilla: turned off...")


class Ventilador(interruptor):
    def turn_on(self):
        print("Ventilador: turned on...")

    def turn_off(self):
        print("Ventilador: turned off...")


class InterruptorEnergia:

    def __init__(self, c: interruptor):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = Bombilla()
f = Ventilador()
switch = InterruptorEnergia(l)
switch.press()
switch.press()