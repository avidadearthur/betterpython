from SwitchableInterface import Switchable


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")
