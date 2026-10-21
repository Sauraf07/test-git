print("Aditya Thakur")

print('doing some major changes in this file')


l1 = [12,45,6,9,8,5,4,5,5,4,63,55,55,98,66,5,56]
largest = l1[0]
second = l1[0]

for i in l1:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i != largest:
        second = i

print(f"largest number = {largest}")
print()
print(f"second largest number = {second}")