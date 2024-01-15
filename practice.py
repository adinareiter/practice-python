# STEM exercises
import random

# 5
list1 = [1, 2, 8, 3, 4]
print(list1.pop())
print(list1)

# 6
string = "hello"
x = list(string)
print(x)

# 7
list2 = [1, 2, 8, 3, 4]
print(list2[2])
del(list2[2])
print(list2)

# 8
list3 = [2, 5, 6, 3]
sum = 0
for i in list3:
  sum += i
print(sum)

# 9
list3 = [2, 5, 6, 3]
max = 0
for i in list3:
  if i > max:
    max = i
print(max)

# 10
list4 = [1,0,3,0,0,5,1,0,8,8]
l = []
for i in list4:
  if i != 0:
    l.append(i)
print(l)

# 11
list5 = [1,0,3,0,0,5,1,0,8,8]
print("Here is a list:", list5) 
num = int(input("Which number would you like to remove from this list? "))
l = []
for i in list5:
  if i != num:
    l.append(i)
print(l)
# or:
# l = [i for i in list5 if i != num]
# print(l)

# 12
list6 = [3, 2, 7, 4]
random.shuffle(list6)
print(list6[1])

#or:
# list6 = [1, 2, 3, 4, 5]
# e = (random.choice(list6))
# print(e)

