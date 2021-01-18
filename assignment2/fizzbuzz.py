def fizzbuzz():
    num = 1
    while(num <= 100):
        if((num % 3 == 0) and (num % 5 == 0)):
            print(num, "FizzBuzz")
        elif(num % 3 == 0):
            print(num, "Fizz")
        elif(num % 5 == 0):
            print(num,  "Buzz")
        else:
            print(num)
        num += 1


def main():
    fizzbuzz()


main()
