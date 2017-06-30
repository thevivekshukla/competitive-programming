# http://codeforces.com/problemset/problem/318/A

import math

n, k = tuple(map(int, input().split()))

o = int(math.ceil(n/2))

if k <= o:
  print((k*2)-1)
else:
  k = k-o
  print(k*2)