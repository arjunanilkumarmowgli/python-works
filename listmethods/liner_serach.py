arr=[2,4,6,3,8,7]
#    0 1 2 3 4 5

# i 
serach_element=int(input("enter number"))
is_present=False
for i in range(0,len(arr)):
    if serach_element==arr[i]:
      
      is_present=True
      break
print(is_present)