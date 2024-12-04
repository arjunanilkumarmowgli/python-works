arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

# commom element without using "in" 13,20,8

for i in range(0,len(arr1)):

    for j in range(0,len(arr2)):

     if arr1[i]==arr2[j]:
      
      print(arr1[i])

