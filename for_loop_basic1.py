#Basic
for i in range(151):
    print(i)

#Multiples of 5
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)

#Counting, the dojo way
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge
sum = 0
for i in range(500001):
    if i % 2 != 0:
        sum = sum + i
print(sum)

#Countdown by fours
for i in range(2018, 0, -4):
    print(i)
    
#Flexible counter
lowNum = 10
highNum = 120
mult = 7
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)