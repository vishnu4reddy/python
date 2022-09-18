thislist = ("apple" ,"banana", "cherry")
print(thislist[1])
print(thislist[0:2])

# exists or not
thistuple = ("apple","banana","cherry")
if"apple"in thistuple:
    print("yes")

#change tuple value
x = ("apple","banana","cherry")
y = list(x)
y[1] ="kiwi"
x = tuple(y)
print(x)
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orrange")
thistuple = tuple(y)

#renove
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)

#unpack
fruits = ("apple","banana","cherry","grapes","rasaberry")
(red,blue,*green) = fruits
print(red)
print(green)
print(blue)
#loop
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#join tuples
tuple1 = ("a","b","c","d","e")
tuple2 = (1,2,3,4,5)
tuple3 = tuple1+tuple2
print(tuple3)
fruits =("apple","banana","cherry")
thistuple = fruits*3
print(thistuple)

# addition of elements in atuple
tuple1 = ('greek', 'for')
print(tuple1)
list1 = [1,2,3,4,5,6]
print(tuple(list1))
tuple1 = tuple('vishnu')
print(tuple)
tuple1 = (0,1,2,3,4)
tuple2 = ('reddy','reddys')
tuple3 = (tuple1,tuple2)
print(tuple3)
