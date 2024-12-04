from re import fullmatch
pattern="(91)+[0-9]{10}"
moblie_number=input("enter moblie number")

matcher=fullmatch(pattern,moblie_number)

if matcher==None:
    print("invalid")
else:
    print("valid")
