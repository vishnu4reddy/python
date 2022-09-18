thisset = {"apple", "banana"}
print(thisset)
thisset = {"apple","cherry","apple","banana"}
print(thisset)

#add
thisset = {"apple","banana","cherry"}
thisset.add("orrange")
print(thisset)

#update
thisset = {"apple","banana","cherry"}
topical = {1,2,3,4,5,6}
thisset.update(topical)
print(thisset)

#remove
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

#loop
thisset = {"apple","banana","vherry"}
for i in thisset:
    print(i)

#intersection_update &intersection
x = {"apple","banana"}
y = {"bus","apple"}
z = x.intersection_update(y)
print(z)
x = {"apple","banana"}
y = {"bus","apple"}
z = x.intersection(y)
print(z)

#symmetric_difference&summertic
x = {"apple","banana"}
y = {"bus","apple"}
z = x.symmetric_difference(y)
print(z)
x = {"apple","banana"}
y = {"bus","apple"}
z = x.symmetric_difference_update(y)
print(z)


mylist = [1,2,3,3,4,5,6,6,7]
myset = set(mylist)
print(myset)

mystr = "vishnu"
myset1 = set(mystr)
print(myset1)
