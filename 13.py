# http://codeforces.com/problemset/problem/116/A

n = int(input())

value = 0
m = -1

for i in range(n):

  li = list(map(int, input().split()))

  value = value - li[0] + li[1]

  if value>m:
    m = value


print(m)

