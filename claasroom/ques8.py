#Write a Python program to find common elements in two lists
#
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
common_elements = list(set(arr1) & set(arr2))
print("Common elements:", common_elements)