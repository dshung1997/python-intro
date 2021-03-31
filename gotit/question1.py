import math

def get_super_prime_numbers():
    first_digits = [2, 3, 5, 7]
    second_digits = [1, 3, 7, 9]
    result = []

    def is_prime(n):
        m = int(math.sqrt(n)) + 1
        for i in range(2, m):
            if n % i == 0:
                return False

        return True

    def construct_numbers(current_numbers):
        new_numbers = []
        for n in current_numbers:
            for d in second_digits:
                new_numbers.append(n * 10 + d)

        return new_numbers

    def check_super_prime():
        numbers = first_digits
        for _ in range(0, 4):
            numbers = construct_numbers(numbers)
            filtered_numbers = []

            for n in numbers:
                if is_prime(n):
                    filtered_numbers.append(n)

            numbers = filtered_numbers

        return numbers

    result = check_super_prime()
    
    return result

# get_super_prime_numbers()