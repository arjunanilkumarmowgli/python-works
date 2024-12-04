from re import findall
f=open("C:\\pythonworks\\regexflieworks\\date_seperation.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,content)

for date in dates:
    print(date) 