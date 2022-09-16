num1,num2 =0,1
for i in range(1,20+1):
    print(num1,end="  ")
    res = num1+num2
    num1 = num2
    num2 = res
    print(res)
