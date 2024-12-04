from re import finditer

text ="i have  3 cars, 2 bike and 1-cycle"
 

# pattern="\w" #or {a-Z} for alphanumeric
#pattern="\d"# for take digits use code or [0-9] it will work 
#pattern="\D"#exclude digit
#pattern="\W"#special characters(^a-ZA-Z0-Z9)
#pattern="\s"#space
pattern="\S"#without SPACE

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())



