st=set()#set
st={10,20,30,10,20,30}
# print(st)#set does not support indexing



#duplicate will delete
text="this is a test to remove duplicate words this is simple"
# split text write space
words=text.split(" ")
print(set(words))