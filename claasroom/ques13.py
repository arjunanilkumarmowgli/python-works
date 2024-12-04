# Write a Python program to find all the even numbers in a list.

arr = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in arr if num % 2 == 0]
print("Even numbers:",even_numbers)