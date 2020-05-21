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
        self.content = []

    def open(self, login, password):
        if login == self.__login and password == self.__password:
            return tuple(self.content)
        else:
            return False

    def save(self, login, password, content):
        if not content:
            return False
        else:
            if login == self.__login and password == self.__password:
                self.content.append(content)
            else:
                return False


safe = Safe("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy")
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", "abc")
safe.save("ArkadiuszNornica", "złehasło", "abc")  # zwraca False
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", 123)
print(safe.open("ArkadiuszNornica", "złehasło"))  # printuje False
print(safe.open("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy"))  # printuje ("abc",123)

