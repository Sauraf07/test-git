def check_prime(number):
    if number <= 1:
        print("This is not a prime number")
        return

    for divisor in range(2, (number // 2) + 1):
        if number % divisor == 0:
            print(number, "is not a prime number")
            return

    print(number, "is a prime number")


num = int(input("Enter the number: "))
check_prime(num)