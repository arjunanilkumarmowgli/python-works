#Write a Python program to find the length of a list without using the len() function.

arr = [1, 2, 3, 4, 5]
length = 0
for _ in arr:
    length += 1
print("Length of th list:",length)