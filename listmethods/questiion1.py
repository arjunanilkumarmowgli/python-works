arr=[100,200,300,400,500]
k=1
#rotate array k time[500,100,200,300,400]
for i in range(0,k+1):
    popped_element=arr.pop()
    arr.insert(1,popped_element)
print(arr)    