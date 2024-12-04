f=open("C:\\pythonworks\\dataset\\fruits.py","r")
fruits=[]
for line in f:
    fruits.append(line.rstrip("/n"))
print(fruits)
                   