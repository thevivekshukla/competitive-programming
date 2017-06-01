# http://codeforces.com/problemset/problem/148/A

k = int(input())
l = int(input())
m = int(input())
n = int(input())

d = int(input())

li = []

for i in range(k-1, d, k):
  li.append(i)


for i in range(l-1, d, l):
  li.append(i)


for i in range(m-1, d, m):
  li.append(i)


for i in range(n-1, d, n):
  li.append(i)


li = set(li)


print(len(li))