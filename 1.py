# http://codeforces.com/problemset/problem/1/A

li = list(map(int, input().split()))

n = li[0]
m = li[1]
a = li[2]

x = int((n+a-1)/a)
y = int((m+a-1)/a)

answer = x*y

print(answer)