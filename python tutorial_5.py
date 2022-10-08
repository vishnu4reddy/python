fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana',4))
print(fruits.reverse())
print(fruits.append('grape'))
print(fruits.sort())
print(fruits.pop())
# using Lists as Stacks
stack = [3,4,5]
print(stack.append(6))
print(stack.append(7))
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
#using lists as queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue.append("Terry") )          # Terry arrives
print(queue.append("Graham")  )        # Graham arrives
print(queue.popleft()  )               # The first to arrive now leaves

print(queue.popleft())                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival

#list Comprechensions
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
#nested list comprehensions
matrix =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
[[row[i] for row in matrix] for i in range(4)]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
print(list(zip(*matrix)))
#del statement
a = [-1,1,66.25,333,333,1234.56]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
# tuples and Sequences
t = (12345, 54321, 'hello!')
print(t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))

print(len(singleton))

print(singleton)

#sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testing

print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both


#Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
tel['jack']

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)
print({x: x**2 for x in (2, 4, 6)})

# Looping statements
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
