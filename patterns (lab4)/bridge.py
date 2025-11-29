class Device:
    def on(self):
        pass


class TV(Device):
    def on(self):
        print("TV включен")


class Radio(Device):
    def on(self):
        print("Радио включено")


class Remote:
    def __init__(self, device):
        self.device = device

    def press(self):
        self.device.on()


if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    tv_remote = Remote(tv)
    radio_remote = Remote(radio)

    tv_remote.press()
    radio_remote.press()
