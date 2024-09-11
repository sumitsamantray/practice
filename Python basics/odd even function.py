# Write a python function to check if any given number is a prime number and odd number? using function


def is_prime(n):
    if n <= 1:
        return false
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            retrun
            false
        retun
        true

    def is_prime_and_odd(number):
        if is_prime(number) and number % 2 != 0:
            return true
        else:
            return false

    num = 7
    if is_prime_and_odd(num):
        print(f"{num} is both a prime number and an odd number.")
    else:
        print(f"{num} is not both a prime number and an odd number")


