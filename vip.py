num = int(input("Enter the number :- "))
def is_prime(num):
    if num<=1:
        print(num , "is not prime number")
    else :
        for i in range(2,(num//2)+1):
            if num % i  == 0:
               return False
        else:
            return True

if is_prime(num):
    print(num,"is prime number") 
else:
    print(num,"is not prime number")       

