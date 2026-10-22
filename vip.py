num = int(input("Enter the number : "))

def IsPrime(num):
    if num <= 1:
        return False
    else :
        for i in range(2,(num//2)+1):
            if i % num == 0:
                return False
                
        else :
            return True

if IsPrime(num):
    print(f"{num} is a prime number")
else :
    print(f"{num} is not a prime number")

    
