from re import finditer
f=open("C:\\pythonworks\\regexflieworks\\social_ppost.txt")
for line in f:
    words=line.rstrip("\n")#check out my new blog post #blog #webdevelopment
    pattern="#\w+"
    matcher=finditer(pattern,words)
    for obj in matcher:
        print(obj.group())
