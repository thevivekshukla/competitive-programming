# http://codeforces.com/problemset/problem/472/A

import math

n = int(input())

if n%2==0:
  print(8, n-8)
else:
  print(9, n-9)


#----------------------------------------------------

# half = n/2

# n1 = int(math.ceil(half))
# n2 = int(math.floor(half))

# # print(n1, n2)

# count = 0
# temp = 0


# while count<1:

#   count1 = 0
#   count2 = 0

#   li = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31]

#   if temp>0:
#     n1+=1
#     n2-=1

#   if n1 in li:
#     li.remove(n1)
#   if n2 in li:
#     li.remove(n2)


#   for i in li:
#     if n1%i==0:
#       count1 += 1
#     if n2%i==0:
#       count2 += 1

#     if (count1>0) and (count2>0):# and (count1==count2):
#       count+=1

#   temp+=1


# print(n1, n2)