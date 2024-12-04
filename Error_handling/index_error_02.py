arr=[1,2,3,4,5,6]

index=int(input("enter index postion="))

try:
    print(arr[index])
except Exception as e :
    print(e)
finally:
    print("high")