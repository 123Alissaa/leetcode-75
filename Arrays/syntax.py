#insertion in static array  not recommeded as it causes the loss of an element
#thus we use dynamic array

A = [1,2,3]
#appending an element
A.append(5)
print(A)

A.pop()
print(A)

#insert not at the end - O(n)

A.insert(2,5)

#modify an element - O(1)
A[0] = 7
print(A)

#accessing an element - O(1)
print(A[2])

#checking if array has an element - O(n)
if 6 in A:
    print("True")
else:
    print("False")

#Strings

#append to end of string - O(n)
s = "hello"

b = s +'z'
print(b)

#check if something in the string
if 'f' in s:
    print("True")

#checking the length of both string and arrays - O(1)
print(len(A))