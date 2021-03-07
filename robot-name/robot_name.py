import random, string


class Robot:
    def __init__(self):
        self.name = ""
        self.set_name()

    def set_name(self):
        letters = list(string.ascii_uppercase)
        num1 = random.randrange(0, 25)
        num2 = random.randrange(0, 25)
        num3 = random.randint(100, 999)

        self.name = F"{letters[num1]}{letters[num2]}{num3}"

    def reset(self):
        random.seed(random.random)
        self.set_name()

random.seed("bla")
R = Robot()

print(R.name)
random.seed("bla")
R.reset()
print(R.name)