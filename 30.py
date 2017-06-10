# http://codeforces.com/problemset/problem/337/A


def _min(a, b):
  if a<b:
    return a
  return b



  
n, m = tuple(map(int, input().split()))

li = list(map(int, input().split()))


li.sort()

best = 9999999

for k in range(0, m-n+1):
  best = _min(best, li[k+n-1]-li[k])


print(best)