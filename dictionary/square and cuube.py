arr=[10,20,30,40,2,3,7,8,9]
even_square={num:num**2 for num in arr if num%2==0}
print(even_square)
odd_cubes={num:num**3 for num in  arr if num%2==0}
print(odd_cubes)
frequency_count={ num:arr.count(num) for num in arr}
print(frequency_count)