number = int(input("Enter the number: "))

if number <= 1:
    print("This is not a prime number")
else:
    for divisor in range(2, (number // 2) + 1):
        if number % divisor == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")