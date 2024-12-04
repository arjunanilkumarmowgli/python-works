#Write a Python program to reverse a list
arr1=[1,2,3,4,5,6,7,8]
rev=[]
for i in range (len(arr1)-1,0,-1):
    rev.append(i)
print(rev)