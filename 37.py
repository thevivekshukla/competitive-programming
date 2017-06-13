# http://codeforces.com/problemset/problem/451/A


li = list(map(int, input().split()))

n = min(li)

if n%2 == 0:
  print("Malvika")
else:
  print("Akshat")