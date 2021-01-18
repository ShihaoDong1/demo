def isPrime(num):
    primes = []
    for possiblePrime in range(2, num+1):
        isPrime = True
        for x in range(2, possiblePrime):
            if(possiblePrime % x) == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return(primes)


num = int(input("Enter a number: "))
print(isPrime(num))
