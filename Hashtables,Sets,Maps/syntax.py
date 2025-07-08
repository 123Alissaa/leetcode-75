#hashing and collision handling
#separate chaining - mainly through linked lists
#immediate lookup in constant time in relation to n - O(1)
#you can add into the hash set
#you can delete stuff from the hash set
#hash map lookup, add, remove all takes O(1)
#Linear probing - when you delete, add some negative value or smthg at that position
#what is hashable(immutable)?- integers, strings, tuple
#not hashable(mutable) - arrays, dictionaries, etc.


#hash sets
s = set()
print(s)

#add items into set - O(1)
s.add(1)
s.add(2)
print(s)

#lookup an item - O(1)
if 1 in s:
    print(True)

#remove an element
s.remove(1)

#set construction - O(S) - S is the length of the string
string = 'aaaaaaababbbbbbaaabababbbbbcccc'
sett = set(string) 

#lookup over items in set - O(n)
for x in s:
    print(x)

#Hashmaps - Dictionaries
d = {'greg': 1, 'steve': 2, 'rob': 3}
print(d)

#add key:val in dictionary: O(1)
d['arsh'] = 4
print(d)

#check for a presence of a key in the dictionary - O(1)
if 'greg' in d:
    print(True)

#check the value corresponding to a key in dictionary
print(d['greg'])

#loop over the key:val pairs in the dictionary - O(n)
for key, val in d.items():
    print(f'key{key}: val {val}')

#default dict
from collections import defaultdict

default = defaultdict(int)
default[2]

#counter
from collections import Counter

counter = Counter(string)
