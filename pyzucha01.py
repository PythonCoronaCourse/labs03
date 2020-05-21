def do_shit(str_1, list_1):
    for x in list_1:
        str_1 = str_1.replace(x, "")
    return str_1


print(do_shit("qwerty", ["we", "qr"]), "kurwo")

