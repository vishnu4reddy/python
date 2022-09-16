num = int(input("enter the no   "))
factorial = 1
if num>0:
    print("the number you entered is invalid")
elif num==0:
    print("the no you have given , the value is 1")
for i in range(1,num+1):
    factorial = factorial*i
    print(num,"is:",factorial)
