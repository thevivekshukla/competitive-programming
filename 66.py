# http://codeforces.com/contest/962/problem/A


n = int(input())

a = list(map(int, input().split()))

half = sum(a)/2

_sum = 0
for i in range(n):
    _sum += a[i]
    if _sum >= half:
        print(i+1)
        break