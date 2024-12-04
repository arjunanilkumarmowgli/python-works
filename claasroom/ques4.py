# Write a Python program to find the second largest element in a list
arr = [1, 2, 2, 3, 3, 3, 4]
occurrences = {i: arr.count(i) for i in arr}
print("Occurrences of each element:",occurrences)