
class Helper:
    def __init(self, work):
        self.work = work
    def __call_(self, work):
        return f"I will help you with your {self.work}"\
                f"Afterwards I will help you with {work}"
helper = Helper("homework")
print(helper("cleaning"))
print(helper("eating"))
