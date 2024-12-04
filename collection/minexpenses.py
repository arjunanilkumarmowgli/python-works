expenses=[10000,11000,12000,13000,30000]
min_expenses=expenses[0]
for i in expenses:
    if i<min_expenses:
        min_expenses=i
print(min_expenses)