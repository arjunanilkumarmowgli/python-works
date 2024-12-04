from re import findall
f=open("C:\\pythonworks\\regexflieworks\\url.txt")
content=f.read()
pattern="https?://[w\S./]+"
urls=findall(pattern,content)
for url in urls:
    print(url)
    