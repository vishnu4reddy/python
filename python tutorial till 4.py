# numbers
sum = 2+2
print(sum)
x = 50-5*6
print(x)
y = (50 - 5*6)/4
print(y)
word = 'python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-6])
#strings
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
          print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
# range
for i in range(5):
    print(i)
list(range(5, 10))


list(range(0, 10, 3))


list(range(-10, -100, -30))
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#break,continue,else clauses on loops
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
#pass statements
while True:
    pass
# match statements
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


