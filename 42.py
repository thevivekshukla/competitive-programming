# http://codeforces.com/problemset/problem/617/A


n = int(input())

count = 0

for i in range(5, 0, -1):
  div = int(n/i)
  if div > 0:
    n -= div*i
    count += div

  if n == 0:
    break


print(count)

