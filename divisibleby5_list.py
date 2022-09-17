num = [5,11,20,21,23,28,40]
for i in range(len(num)):
    if num[i]%5==0:
        print(num[i])
else:
    pass
num = [5,11,20,21,23,28,40]
for i in range(len(num)):
    if num[i]%2==0:
        print(num[i])
else:
    pass
num = [5,11,20,21,23,28,5,11,21,22,40]
even = []
odd = []
for i in range(len(num)):
    if num[i]%2==0:
        even.append(num[i])
    else:
            odd.append(num[i])
    print(num[i])
else:
    pass
    print("even are",even)
    print("odd are",odd)
