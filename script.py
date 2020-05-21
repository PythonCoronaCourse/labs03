def string_cleanup(arg1, arg2):
    for i in arg2:
        arg1 = arg1.replace(i,"")
    print(arg1)


string_cleanup("abcdbabc_ac_ab_ca", ["ab", "ac"])
