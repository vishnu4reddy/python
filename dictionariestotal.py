thisdict = {
    "brand" : "ford",
    "model" : "mustag",
    "year" : "1947",
    }
print(thisdict)
thisdict = {
    "brand" : "ford",
    "model" : "mustag",
    "year" : "1947",
    }
print(thisdict["brand"])

#duplicates not allowed
thisdict = {
    "brand" : "ford",
    "model" : "mustag",
    "year" : "1947",
    "year" : "2022",
    }
print(thisdict)
print(len(thisdict))
print(type(thisdict))

# update
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2022,
    }
x = car.keys()
print(x)
car["colour"] = "white"
print(x)


#remove
thisdict = {
    "brand" : "ford",
    "model" : "mustag",
    "year" : "1947",
    "year" : "2022",
    }
thisdict.pop("brand")
print(thisdict)


#copy
thisdict = {
    "brand" : "ford",
    "model" : "mustag",
    "year" : "1947",
    "year" : "2022",
    }
mydict = thisdict.copy()
print(mydict)

#nested
myfamily = {
    "child1" : {
    "name" : "vishnu",
    "year" : 1999,
    },
    "child2" : {
    "name" : "vardhan",
    "year" : 2000,
    },
    "child3" : {
    "name" : "reddy",
    "year" : 2002,
    },
}
print(myfamily)
