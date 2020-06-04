def my_count(str1, str2):
    count = 0
    l = len(str2)
    while str2 in str1:
        k = str1.index(str2)
        str1 = str1[:k] + str1[k + l:]
        count += 1
    print (count)


my_count("mam kota Mamrota co lubi jeść szprota", "ota")