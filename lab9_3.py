class MyClass:
    def __init__(self, value):
        self._value = value
        print(f"Объект создан со значением: {self._value}")
    def set_value(self, value):
        self._value = value
        print(f"Значение установлено: {self._value}")
    def get_value(self):
        return self._value
    def del_value(self):
        del self._value
        print("Атрибут _value удален")
    value = property(get_value, set_value, del_value, "Свойство value")
    def __del__(self):
        print("Объект удаляется (деструктор)")
obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
obj.value = 100
obj.del_value()