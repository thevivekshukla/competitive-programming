# http://codeforces.com/problemset/problem/136/A

n = int(input())

li = list(map(int, input().split()))

_li = []
for i in li:
  _li.append(i)

for i in range(0, n):

  _li[li[i]-1] = i+1
  # print("i", "li[i]", "li[i]-1", "_li[li[i]-1]")
  # print(i, li[i], li[i]-1, _li[li[i]-1])



for i in _li:
  print(i,end=" ")