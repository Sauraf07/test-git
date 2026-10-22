num = int(input("Enter the number : "))

def IsPrime(num):
    if num <= 1:
        print(num ,"is not  a prime number")
    else :
        for i in range(2,(num//2)+1):
            if i % num == 0:
                print(num ,"is not a prime number")
                break
        else :
            print(num ,"is a prime number")

IsPrime(num)

    
