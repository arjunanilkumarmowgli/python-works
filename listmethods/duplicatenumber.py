arr=[1,2,2,2,3,1,3,4,5]
arr.sort()
duplicate_number=[]
#duplicate numbers
# 0 1 2 2 
#   i j
for i in range(0,len(arr)-1):

    j=i+1 
    result=arr[j]-arr[i]
   # if result!=1:
       # print(arr[i],"is duplicate")
 #      or

    if result==0:
          
          if arr[i] not in duplicate_number:
               duplicate_number.append(arr[i])

print( duplicate_number)