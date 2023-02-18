import random
class Tymofii:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.job = Job

    def to_money(self):
        print("time to make money")
        print("Your job is")

        self.progress += 0.12
        self.gladness -=3

    def to_sleep(self):
        print("I will sleep")
        self.gladness +=3

    def to_play(self):
        print("I will play in computer!")
        self.gladness +=5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
        elif self.progress > 3:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness={self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")



    def live(self, day):
        day = "Day" +str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1 , 3)
        if live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_play()
        self.end_of_day()


class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]



job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


nick = Tymofii(name="Tymofii")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)