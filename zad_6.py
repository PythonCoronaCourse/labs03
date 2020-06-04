def bingify(r_list, r_word):
    n_list = []
    for word in r_list:
        if word[-1] == (r_word):
            n_word = word + ("_bingo")
            n_list.append(n_word)
        else:
            n_list.append(word)
    print(n_list)

bingify(["abc", "abca", "a", "cad", "baca", "bc"], "a")