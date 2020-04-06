class CustomType:
    def __init__(self, value):
        self.value = value

    def add(self, value):
        self.value += value

    def sub(self, value):
        self.value -= value


foo = CustomType(42)
print(foo.value)
print(foo.__hash__())
print(foo)
