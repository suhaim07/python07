def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


number = int(input("Enter a number: "))
if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")