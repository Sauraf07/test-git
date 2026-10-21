num = int(input("Enter the number : -"))

for i in range(2,num//2-1):
    if i % num != 0:
        print(num ,"is prime number")
        break