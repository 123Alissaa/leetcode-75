#Lookup time is O(n)
#m = (l + r) // 2
#time : O(log n to the base 2)
#space : O(1)

A = [-3, -1, 0, 1, 4, 7]

#Naive O(n) searching
if 8 in A:
    print(True)

#Traditional binary search - looking up if number is in array:
#Time - O(log n)
#Space - O(1)

N = len(A)
L = 0
R = N - 1

def binary_search(arr, target):
    while L <= R:
        M = L +((R-L) // 2)

        if arr[M] == target:
            return True
        elif target < arr[M]:
            R = M - 1
        else:
            L = M + 1
    return False

binary_search(A, 7)

#based on a condition
B = [False, False, False, False, True, True, True]

def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1

    while L < R:
        M = (L + R) // 2

        if B[M]:
            R = M
        else: 
            L = M + 1
        
    return L
binary_search_condition(B)