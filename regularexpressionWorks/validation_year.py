from re import fullmatch
year=input("enter year:")
pattern="(18[0-9]{2}|19[0-9]{2}|20[0-2]{1}[0-4]{1})"
matcher=fullmatch(pattern,year)
print("invalid" if matcher==None else "valid")
