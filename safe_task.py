class Safe:
    def __init__(self, __login, __password):
        self.__login = __login
        self.__password = __password
        self.__set = []

    def open(self, login, password):
        if login == self.__login and password == self.__password:
            print(tuple(self.__set))
            return tuple(self.__set)
        else:
            print("Zle haslo kurwiu")
            return False

    def save(self, login, password, new_object):
        if login == self.__login and password == self.__password:
            self.__set.append(new_object)
        else:
            print("Zle haslo kurwiu")
            return False


safe = Safe("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy")
safe.open("ArkadiuszNornica", "zlehaslo")
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", "abc")
safe.save("ArkadiuszNornica", "złehasło", "abc")  # zwraca False
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", 123)
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", "zupa knorra")
safe.open("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy")
