gmail_id=input("enter date:")
pattern="([a-z]+)"
matcher=fullmatch(pattern,gmail_id)
print("invalid" if matcher==None else "valid")








