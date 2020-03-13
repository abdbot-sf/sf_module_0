import numpy as np
number = np.random.randint(1,100)
n=0
max1=100
min1=0
ugadai=0
while True:
    ugadai=int((max1+min1)/2)
    if ugadai==number:
        break
    elif ugadai>number:
        max1=ugadai
    elif ugadai<number:
        min1=ugadai
    n+=1
print(number, n)