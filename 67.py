# http://codeforces.com/contest/962/problem/B

n, a, b = map(int, input().split())
s = a + b
for t in map(len, input().split("*")):
    if b > a: a, b = b, a
    if t % 2: a -= 1
    t //= 2
    a -= t
    b -= t


print(s - max(0,a) - max(0,b))