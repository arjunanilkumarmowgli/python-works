from re import fullmatch
pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
kerala_registation=input("enter kerala resgistation number")

matcher=fullmatch(pattern,kerala_registation)

if matcher==None:
    print("invalid")
else:

    print("valid")
