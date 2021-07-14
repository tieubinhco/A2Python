class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.talk()

    def talk(self):
        print(f"Hello, my name is  {self.name}")


class Dog(Pet):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.color = color

    def showDog(self):
        print("bark bark")


P1 = Dog("Susu", 6, "White")
P1.talk()


# Pet1.talk()
# Pet2.talk()
MRO
