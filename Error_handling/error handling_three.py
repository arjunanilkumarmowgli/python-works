num1=int(input("enter num1="))
num2=int(input("enter num2="))

try:#error code
    result=num1/num2#10/0=error
    # print(result)#5.0salt increase
except:#this mean error handling
    num2=int(input("enter nnumber"))
    result=num1/num2
    print(result)

finally:#this mean

    print("file operation")

    print("database commit")

 