user_input=input("enter the input")
stack=[]
top=len(stack)-1
symbols={"[":"]","{":"}","(":")","<":">"}
for i in user_input:                    # the input has checked in 
    if i in symbols.keys():          # and the input has checked in with the dictinary called symbols and the keys are taken  
        stack.append(i)                 # the value are apped in it 
    elif i==symbols.get(i) and i==symbols.get(stack[top]):      #her the input is checkeed in the values and if its present in it and it should be cheacked with the top of the stack as well
        stack.pop(top) # then pop the lement out of it 
    else:
        break
print("valid" if len(stack)==0 else "not valid")# and if after poping every elemnet check the stack lengthh if its 0 then print valid or print invalid
