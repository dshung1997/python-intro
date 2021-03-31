import math

def func():
    some_primes = [2, 3, 5, 7, 11, 13, 17, 19]    
    # 2, 3, 5, 7,
    # 1, 3, 7, 9

    def is_prime(n):
        m = int(math.sqrt(n)) + 1
        for i in some_primes:
            if i > m:
                break
            
            if n % i == 0:
                return False
        return True

    five_digits = []
    for n in range(20, 100000):
        if is_prime(n):
            some_primes.append(n)
            if n > 10000:
                five_digits.append(n)
    
    result = []

    for n in five_digits:
        x = n
        save = True

        while True:
            x = x // 10

            if x == 0:
                break

            if x not in some_primes:
                save = False
                break
        
        if save:
            result.append(n)

    print(result)

func()