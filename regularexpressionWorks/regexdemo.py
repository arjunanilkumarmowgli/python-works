from re import finditer

text="ababababab"
# 0   0123456789
# [(0,ab),(2,ab),(4,ab),(8,ab)]
# (start,group)
matcher=finditer("ab",text)

for m in matcher:#m=(start=0,group=ab)
    print(m.start(),m.group()) 