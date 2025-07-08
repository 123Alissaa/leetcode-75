#Stacks
#append is a common operation used - O(1)
#pop - O(1)
#peek - O(1) - asking what's on top 
#S[-1] to get the last element
#isEmpty - O(1)
#LIFO - Last In First Out

stk = []

#append to top of the stack
stk.append(5)

#pop from the stack
x = stk.pop()

#ask whats on top of the stack
print(stk[-1])

#ask if something is in the stack - O(1)
if stk:
    print(True)
