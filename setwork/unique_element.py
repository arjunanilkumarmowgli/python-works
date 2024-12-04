arr=[10,10,20,30,40,50,40]

#10,20,30,40,50

# create a emtyset
st=set()

# fetch element from array  

for num in arr:
    # add num to arr
    st.add(num)
#display arr
print(st)   

st1={10,20,30,40,50}
st2={10,20,60,70,80}
intersection_set=st1.intersection(st2)
print(intersection_set)