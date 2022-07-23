from LightBulb import LightBulb
from Fan import Fan
from ElectricPowerSwitch import ElectricPowerSwitch


class main:
    def __init__(self):
        pass

    def run(self):
        l = LightBulb()
        f = Fan()
        switch = ElectricPowerSwitch(f)
        switch.press()
        switch.press()


if __name__ == "__main__":
    main = main()
    main.run()
