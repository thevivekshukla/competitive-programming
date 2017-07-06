# http://codeforces.com/problemset/problem/379/A

a, b = tuple(map(int, input().split()))

res = a

while True:

  t = int(a/b)
  r = a%b

  res += t

  a = t + r

  if a<b:
    break

print(res)