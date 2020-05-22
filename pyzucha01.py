# ------------------------------- zadanie nr 1 --------------------------------
def do_shit(str_1, list_1):
    for x in list_1:
        str_1 = str_1.replace(x, "")
    return str_1


print(do_shit("qwerty", ["we", "qr"]), "kurwo")


# ------------------------------- zadanie nr 2 --------------------------------
class Safe:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__content = []

    def open(self, login, password):
        if login == self.__login and password == self.__password:
            return tuple(self.__content)
        else:
            return False

    def save(self, login, password, content):
        if login == self.__login and password == self.__password:
            self.__content.append(content)
        else:
            return False


safe = Safe("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy")
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", "abc")
safe.save("ArkadiuszNornica", "złehasło", "abc")
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", 123)
print(safe.open("ArkadiuszNornica", "złehasło"))
print(safe.open("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy"))


# ------------------------------- zadanie nr 3 --------------------------------
def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


for i in range(1, 21):
    print(fizzbuzz(i))


# ------------------------------- zadanie nr 4 --------------------------------
def count_shit(str_1, list_1):
    counter = 0
    for x in list_1:
        if x in str_1:
            counter += 1
    return counter


print(count_shit("mam kota Mamrota co lubi jeść szprota", "ota"))


# ------------------------------- zadanie nr 5 --------------------------------
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    @staticmethod
    def get_all():
        cats = []
        lines = open("zad03.txt", "r").read().splitlines()
        for line in lines:
            cats.append(Cat(*line.split(",")))
        return cats


for cat in Cat.get_all():
    print(cat.name, cat.age, cat.color)


# ------------------------------- zadanie nr 6 --------------------------------
def bingify(list_1, str_1):
    bingified = []
    for x in list_1:
        if x[-1] == str_1:
            bingified.append(f"{x}_bingo")
        else:
            bingified.append(x)
    return bingified


print(bingify(["abc", "abca", "a", "cad", "baca", "bc"], "a"))
