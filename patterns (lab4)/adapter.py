class EuropeanSocket:
    def plug_in(self):
        return "Подключено к европейской розетке"


class ChinesePlug:
    def connect(self):
        return "Подключено к китайской розетке"


class EuropeanAdapter:
    def __init__(self, chinese_plug: ChinesePlug):
        self.chinese_plug = chinese_plug

    def plug_in(self):
        result = self.chinese_plug.connect()
        return f"Адаптер: {result} работает с европейской розеткой"


if __name__ == "__main__":
    socket = EuropeanSocket()
    plug = ChinesePlug()
    adapter = EuropeanAdapter(plug)
    print(socket.plug_in())
    print(adapter.plug_in())
