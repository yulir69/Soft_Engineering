class Ivan:
    __slots__ = ['name']
    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}!"
        else:
            self.name = f"Я не {name}, а Иван"
        print(self.name)

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
