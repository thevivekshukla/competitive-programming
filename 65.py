# http://codeforces.com/problemset/problem/492/B


n, l = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

d = 0

if a[0] != 0:
    d = a[0]
if a[-1] != l:
    t = l - a[-1]
    if d < t:
        d = t


for i in range(n-1):
    t = (a[i+1] - a[i])/2
    if d < t:
        d = t


print("{:.9f}".format(d))