def FizzBuzz(a, b, c):
    for i in range (1, c):
        if i % (a*b) == 0:
            print("FizzBuzz")
        elif i%a == 0:
            print ("Fizz")
        elif i%b == 0:
            print ("Buzz")
        else:
            print (i)

maxnumber = int(input("Type end of range: "))
number_1 = int(input("Type number 1: "))
number_2 = int(input("Type number 2: "))
FizzBuzz(number_1, number_2, maxnumber)