x = lambda a : a+10
print(x(55))
#
x = lambda a,b : a*b
print(x(25,55))
#
x = lambda a,b,c : a*b+c
print(x(25,55,22))
# Lambda Functions
def myfunc(n) :
    return lambda a:a*n
    mylower = myfunc(2)
    print(mylover(11))
#
animals = ['dog','cat','parrot','rabbit']
upperanimals = list(map(lambda animals: animals.upper(),animals))
print(upperanimals)
