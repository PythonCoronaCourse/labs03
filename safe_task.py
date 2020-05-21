class Safe:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__lista = []

    def open(self, login, password):
        if login == self.__login and password == self.__password:
            print(tuple(self.__lista))
            return tuple(self.__lista)
        else:
            print("Zle haslo kurwiu")
            return False

    def save(self, login, password, new_object):
        if login == self.__login and password == self.__password:
            self.__lista.append(new_object)
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
