arr=[2,3,4,5,6,7]
# comperhension list is find the squares of number
square_num=[num**2 for num in arr]
print(square_num)
# find the cube of number
cube_num=[num**3 for num in arr]
print(cube_num)
#   return iteration condition
# odd number
odd_number=[num for num in arr if num%2==0]
print(odd_number)
# even number
even_number=[ num for num in arr if num%2!=0]
print(even_number)
# number is greater than 5
num_gt_five=[num for num in arr if num>5] 
print(num_gt_five)
