student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40],
}
#index=1 hari's avg mark

for index,element in enumerate(student_data):
 
 print(index,element)

index=2
for i, element in enumerate(student_data):
  if i+1==index:
    print(element)

index=5  
for i,element in enumerate(student_data):
   if i+1==index:
     marks=student_data.get(element)
     avg=sum(marks)/len(marks)
     print(avg)

student_avg_marks={k:sum(v)/len(v) for k,v in student_data.items()}
print(student_avg_marks)


source_word="REGULATE"

target_word="LATTER"

# kangaroo_word...


























