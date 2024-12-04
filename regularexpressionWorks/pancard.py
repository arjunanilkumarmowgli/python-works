from re import fullmatch

pancard_number=input("enter the pandcard number:")

pattern="[A_Z]{3}[PCAFHT][A_Z]{1}[0_9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:
    print("invalid")
else:
    print("valid")
                  