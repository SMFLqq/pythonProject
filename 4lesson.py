class Wow:
    def __wow(self):
        print("Wow")
    def _hello(self):
        print("Hello")

some_obj = Wow()
some_obj._hello()
some_obj._Wow__wow()

class Hello:
    def __init__(self):
        print("Hello")
class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")
hello_world = Hello_World()

class Grandparent:
    def about(self):
        print("I am GrandParent")
    def about_myself(self):
        print("I am GrandParent")
class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
nick = Child()