import math


m, n = map(int, input().split())



primes = []

for num in range(m,n+1):

    if num>1:

        is_prime = True

        if num == 2:
            primes.append(num)
            continue

        if num % 2 == 0:
            continue

        for i in range(3, int(math.sqrt(num))+1, 2):

            if num % i == 0:

                is_prime = False
                break

        if is_prime:
            primes.append(num)

        
for i in primes :
    print(i, end=" ")