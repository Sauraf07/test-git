num = int(input("Enter the number :- "))

if num < 2:
    print(num , "not a prime num")
else:
    for i in range(2,(num//2)+1):
        if i % num != 0:
            print(num ,"is prime number")
            break

    else:
        print(num, "prime number ")