class Database:
    def get_secret_data(self):
        return "NDA"


class ProxyDatabase:
    def __init__(self, database, password: str):
        self.database = database
        self.password = password

    def get_secret_data(self, password: str):
        if password == self.password:
            return self.database.get_secret_data()
        return "Доступ запрещен"


if __name__ == "__main__":
    db = Database()
    proxy = ProxyDatabase(db, "qqq")
    print(proxy.get_secret_data("www"))
    print(proxy.get_secret_data("qqq"))
