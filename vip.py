def is_prime_no(num):
    for i in range(2,(num//2)+1):
        if i % num != 0:
            print(num ,"is prime number")
            return True
    return False

num = int(input("Enter the number : -"))
is_prime_no(num)