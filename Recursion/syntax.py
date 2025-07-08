#fibonacci
#f(0) = 0
#f(1) = 1
#F(n) = F(n-1) + F(n-2)
#recursive call stack
#time is O(2^n)
#space is O(n)
#linked lists, trees, graphs are also recursive

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

#linked lists
#Time : O(n)
def reverse(node):
    if not node:
        return
    
    reverse(node.next)
    print(node)

reverse(Head)