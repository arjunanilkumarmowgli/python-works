from re import fullmatch
date=input("enter date:")
pattern="(0?[1-9]|[12][0-9]|3[01])"
matcher=fullmatch(pattern,date)
print("invalid" if matcher==None else "valid")