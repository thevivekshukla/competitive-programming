# http://codeforces.com/problemset/problem/263/A

li = [[], [], [], [], []]

b_li = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(5):
  li[i] = list(map(int, input().split()))

c = 0
r = 0
count = 0

for i in range(5):
  for j in range(5):
    if li[i][j]==1:
      r = i
      c = j


while li != b_li:
  if r>2:
    li[r][c]=0
    r-=1
    li[r][c]=1
    count+=1
  elif r<2:
    li[r][c]=0
    r+=1
    li[r][c]=1
    count+=1


  if c>2:
    li[r][c]=0
    c-=1
    li[r][c]=1
    count+=1
  elif c<2:
    li[r][c]=0
    c+=1
    li[r][c]=1
    count+=1


print(count)