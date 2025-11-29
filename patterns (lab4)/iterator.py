class Workers:
    def __init__(self):
        self.workers = []

    def add(self, worker: str):
        self.workers.append(worker)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.workers):
            worker = self.workers[self.index]
            self.index += 1
            return worker
        raise StopIteration

if __name__ == "__main__":
    team = Workers()
    team.add("Иван")
    team.add("Мария")
    team.add("Алексей")
    team.add("Светлана")

    print("Список рабочих:")
    for worker in team:
        print(worker)