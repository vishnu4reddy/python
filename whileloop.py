import random
i = 1
while i<= 5:
    newrand = random.randint(0,5)
    print(newrand)
    if newrand == 3:
       print("break")
       break
       i += 1