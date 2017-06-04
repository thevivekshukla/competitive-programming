# http://codeforces.com/problemset/problem/337/A

n, m = tuple(map(int, input().split()))

li = list(map(int, input().split()))


li.sort()

difference = []

for i in range(1, m):

  difference.append(abs(li[i-1]-li[i]))


difference.sort()
print(difference)

s = 0

if (n==2):
  print(min(difference))
else:
  for i in range(n-1):
    s += difference[i]
  print(s)
