# http://codeforces.com/problemset/problem/486/A


n = int(input())

_sum = int(n/2)


if n%2 == 0:
  print(_sum)
else:
  print("-"+str(_sum+1))

