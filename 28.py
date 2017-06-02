# http://codeforces.com/problemset/problem/69/A


n = int(input())

li = []

x = 0
y = 0
z = 0

for i in range(n):
  li.append([])

  li[i] = list(map(int, input().split()))

  x += li[i][0]
  y += li[i][1]
  z += li[i][2]




if x==0 and y==0 and z==0:
  print("YES")
else:
  print("NO")
