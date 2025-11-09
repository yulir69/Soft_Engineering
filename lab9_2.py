class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')

icecream1 = Icecream()
icecream1.composition()

icecream2 = Icecream('шоколадом')
icecream2.composition()

icecream3 = Icecream(5)
icecream3.composition()