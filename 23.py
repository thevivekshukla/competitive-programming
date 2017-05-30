# http://codeforces.com/problemset/problem/546/A

k, n, w = tuple(map(int, input().split()))

s = 0

for i in range(1, w+1):
  s += i*k

res = s-n

if res>=0:
  print(res)
else:
  print(0)