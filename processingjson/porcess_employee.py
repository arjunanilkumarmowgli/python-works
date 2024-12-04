from json import load
 
f=open("C:\\pythonworks\\dataset\\employee.json")
data=load(f)
for emp in data:
    print(emp)