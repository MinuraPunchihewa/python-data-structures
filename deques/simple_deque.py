from collections import deque

d = deque()

# the deque can also be initialized with a sequence
d = deque([3, 4, 5])

# push an element onto the right of the deque
d.append(1)

# push an element onto the left of the deque
d.appendleft(2)

# pop an element off the right of the deque
d.pop()

# pop an element off the left of the deque
d.popleft()

# reverse the order of the elements in the deque
d.reverse()

# rotate the deque n steps to the right
d.rotate(1)

# rotate the deque n steps to the left
d.rotate(-1)

# extend the deque by appending elements from an iterable to the right
d.extend([6, 7, 8])