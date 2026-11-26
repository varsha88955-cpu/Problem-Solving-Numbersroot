
# 1. Spy Number
# Write a function to check whether a number is a Spy Number.
# Sum of digits = Product of digits

def is_spy(n):
    temp = n
    total = 0
    product = 1

    while temp > 0:
        digit = temp % 10
        total += digit
        product *= digit
        temp //= 10

    return total == product


# 2. Strong Number
# Write a function to check whether a number is a Strong Number.
# Sum of factorials of digits = Original number

def is_strong(n):
    if n <= 0:
        return False

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        fact = 1

        for i in range(1, digit + 1):
            fact *= i

        total += fact
        temp //= 10

    return total == n


# 3. Harshad Number
# Write a function to check whether a number is a Harshad Number.
# Number is divisible by the sum of its digits

def is_harshad(n):
    if n <= 0:
        return False

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    return n % total == 0


# 4. Neon Number
# Write a function to check whether a number is a Neon Number.
# Sum of digits of its square = Original number

def is_neon(n):
    if n < 0:
        return False

    square = n * n
    total = 0

    while square > 0:
        digit = square % 10
        total += digit
        square //= 10

    return total == n


# 5. Digital Root
# Write a function to find the Digital Root of a number.
# Repeatedly add digits until a single digit remains

def digital_root(n):
    n = abs(n)

    while n >= 10:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit
            n //= 10

        n = total

    return n


# 6. Magic Number
# Write a function to check whether a number is a Magic Number.
# Repeatedly add digits until the result becomes 1

def is_magic(n):
    if n <= 0:
        return False

    while n > 9:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit
            n //= 10

        n = total

    return n == 1
