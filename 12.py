# http://codeforces.com/problemset/problem/158/B

import math

n = int(input())

li = list(map(int, input().split()))

count = 0
one_count = 0
two_count = 0
three_count = 0

for i in li:
  if i==4:
    count+=1
  elif i==3:
    three_count+=1
  elif i==2:
    two_count+=1
  elif i==1:
    one_count+=1
  # li.remove(i)


count += three_count
one_count -= three_count



if two_count>=2:
  if two_count%2 == 0:
    count += int(two_count/2)
    two_count = 0
  else:
    count += int((two_count-1)/2)
    two_count = 1



if one_count>0 and two_count>0:
  one_count -= 2
  count += 1
  two_count = 0



if two_count > 0:
  count += 1

if one_count>=4:
  rem = int(one_count/4)
  count += rem #+ (one_count%4)
  one_count = one_count%4

if one_count>0:
  count += 1


print(int(count))