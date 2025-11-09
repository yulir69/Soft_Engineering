class Russian:
    @staticmethod
    def greeting():
        print("Привет")
class English:
    @staticmethod
    def greeting():
        print("Hello")
def greet(language):
    language.greeting()
ivan = Russian()
john = English()
greet(ivan)
greet(john)
Russian.greeting()
English.greeting()