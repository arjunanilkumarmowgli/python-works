employee={"eid":12, "name":"sibu","salary":30000,"department":"user","experience":2}
print(employee)
employee["contact"]=2345676543#a dd method 
print(employee)
if employee["experience"]>5:
    employee["salary"]+=100000
else:
                 employee["salary"]+=5000   
print(employee)
if employee["experience"]>5:
        employee["experience"]="SDE"
else:
        employee["experience"]="JDE"
print(employee)