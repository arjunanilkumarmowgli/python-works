from re import finditer

text="abbbbaababbaabaaaaab"

#pattern="a{2}"#finding aa in placed
#pattern="a{1,3}"# finding 1 time(a)or 3 time (a)
pattern="a"

matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())