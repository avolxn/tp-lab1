class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler

    def handle(self, request: str):
        if self.next:
            return self.next.handle(request)
        return "Запрос не обработан"


class LogHandler(Handler):
    def handle(self, request: str):
        if "LOG" in request:
            return f"[LOG] {request.replace('LOG', '')}"
        return super().handle(request)


class ErrorHandler(Handler):
    def handle(self, request: str):
        if "ERROR" in request:
            return f"[ERROR] {request.replace('ERROR', '')}"
        return super().handle(request)


if __name__ == "__main__":
    log = LogHandler()
    error = ErrorHandler()
    log.set_next(error)
    print(log.handle("LOG Приложение запущено"))
    print(log.handle("ERROR Файл не найден"))
    print(log.handle("UNKNOWN Запрос"))
