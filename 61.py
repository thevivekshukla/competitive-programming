# http://codeforces.com/problemset/problem/677/A


n, h = map(int, input().split())

li = map(int, input().split())

width = n

for i in li:
    if i > h:
        width += 1

print(width)