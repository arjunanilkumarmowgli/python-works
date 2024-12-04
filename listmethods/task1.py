#sample question1
arr1=[1,3,4,5]
#find least +ve missing integer 2

n=1 
for i in range(0,len(arr1)):
    if n==arr1[i]:
        n=n+1
    else:
           break
print(n)