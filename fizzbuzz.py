def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    else:
        if num % 3 == 0:
            return "fizz"
        else:
            if num % 5 ==0:
                return "buzz"
            else:
                return num


for i in range(1, 21):
  print(fizzbuzz(i))