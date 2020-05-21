# zadanie nr 1
def do_shit(str_1, list_1):
    for x in list_1:
        str_1 = str_1.replace(x, "")
    return str_1


print(do_shit("qwerty", ["we", "qr"]), "kurwo")


# zadanie nr 2
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
safe.save("ArkadiuszNornica", "złehasło", "abc")  # zwraca False
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", 123)
print(safe.open("ArkadiuszNornica", "złehasło"))  # printuje False
print(safe.open("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy"))  # printuje ("abc",123)


# zadanie nr 3
def fizzbuzz(x):
    if x%15 == 0:
        return "FizzBuzz"
    elif x%3 == 0:
        return "Fizz"
    elif x%5 == 0:
        return "Buzz"
    else:
        return x

for i in range(1, 21):
    print(fizzbuzz(i))
