# http://codeforces.com/problemset/problem/82/A

import math

n = int(input())

li = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


# s1 l2 p3 r4 h5 
# s6 s7 l8 l9 p10 p11 r12 r13 h14 h15
# s16 s17 s18 s19 l20 l21 l22 l23 p24 p25 p26 p27 r28 r29 r30 r31 h32 h33 h34 h35
# s36

def check(var, factor, name):
  till = int(math.ceil(math.log(n, 2)))

  li = [factor*(2**x) for x in range(till)]
  li[0] = var
  for i in range(1, till):
    li[i] = li[i]+li[i-1]

  # print(li)

  for i in range(till):
    if li[i] <= n < (li[i]+(2)**(i+1)):
      print(name)
      return True


if n <=5:
  print(li[n-1])
elif check(6, 5, "Sheldon"):
  pass
elif check(8, 6, "Leonard"):
  pass
elif check(10, 7, "Penny"):
  pass
elif check(12, 8, "Rajesh"):
  pass
elif check(14, 9, "Howard"):
  pass

# s - 1 6 16 36 76 156 316