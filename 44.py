# http://codeforces.com/problemset/problem/460/A


n, m = tuple(map(int, input().split()))

res = n

if n<m:
  print(n)
else:
  while True:

    i = int(n/m)
    j = n%m
    res += i

    if n==0 or n==1 or n==i+j:
      break

    n = i+j

  print(res)

