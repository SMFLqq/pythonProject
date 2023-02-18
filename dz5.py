import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.job = job
        self.car = car

    def get_car(self):
        self.car = (brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)


    def chill(self):
        self.gladness += 10

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.car is None:
            self.get_car()
            print(f"I bought a car")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")


    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }

nick = Human(name="Nick")
for day in range(1, 800):
    if nick.live(day) == False:
        break