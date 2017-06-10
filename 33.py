# http://codeforces.com/problemset/problem/580/A

n = int(input())

li = list(map(int, input().split()))

max_li = []
count = 1


for i in range(0, n-1):

  if li[i+1] >= li[i]:
    count += 1
  else:
    max_li.append(count)
    count = 1

max_li.append(count)

print(max(max_li))