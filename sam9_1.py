class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3

    def get_state(self):
        return self.states[self._state]

class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай! Все томаты созрели.")
            self._plant.give_away_all()
            return True
        else:
            print(f"{self.name}: Томаты еще не дозрели")
            return False

    @staticmethod
    def knowledge_base():
        print("Помидоры проходят 4 стадии созревания:")
        print("   - отсутствует")
        print("   - цветение")
        print("   - зеленый")
        print("   - красный (созрел)")
        print("Садовник должен ухаживать за растением,")
        print("   пока все томаты не созреют")
        print("Собирать урожай можно только когда все")
        print("   томаты стали красными")

if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Василий", bush)

    print(f"Создан садовник {gardener.name} с кустом из {len(bush.tomatoes)} помидоров")
    gardener.work()
    print("\nПопытка сбора урожая")
    gardener.harvest()

    print("\nПродолжаем ухаживать")
    for day in range(1, 4):
        print(f"\nДень {day}:")
        gardener.work()
        print(f"Состояние томатов: ", end="")
        states = [tomato.get_state() for tomato in bush.tomatoes]
        print(", ".join(states))
        if gardener.harvest():
            break
    if bush.tomatoes:
        print("\nФинальная попытка сбора")
        gardener.harvest()