def factors_factorization(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        prime_factors.append(n)

    return prime_factors


num = int(input("Enter a number and find it's prime factorization: "))
print(factors_factorization(num))
