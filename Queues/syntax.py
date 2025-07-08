#FIFO property
#enqueue(x) - more like append
#dequeue - pop from the end or from the left

from collections import deque

q = deque()

print(q)

#enqueue - add an element to the right - O(1)
q.append(5)

#dequeue - remove from the left
q.popleft()

#peek from left side
q[-1]
