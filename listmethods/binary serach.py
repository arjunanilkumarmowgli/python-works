arr=[10,13,15,16,18,20,22,26]
arr.sort()
serch_elememt=int(input("enter number"))
is_present=False
low=0

upp=len(arr)-1
while(low<=upp):
     
   mid=(low+upp)//2

   if serch_elememt==arr[mid]:
      is_present=True
      break
   elif serch_elememt<arr[mid]:
      
      upp=mid-1

   elif serch_elememt>arr[mid]:
      
      low=mid+1 
print(is_present)          

 