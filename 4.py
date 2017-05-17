# http://codeforces.com/problemset/problem/158/A

n, k = tuple(map(int, input().split()))


li = list(map(int, input().split()))

count = 0

kth = li[k-1]

for i in li:
  if (i>0 and i>=kth):
    count += 1


print(count)