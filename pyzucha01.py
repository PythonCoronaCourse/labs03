def do_shit(str_1, list_1):
    for x in list_1:
        str_1 = str_1.replace(x, "")
    print(str_1)


do_shit("qwerty", ["we", "qr"])
print("kurwo")
