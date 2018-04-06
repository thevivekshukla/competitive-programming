# http://codeforces.com/problemset/problem/230/A


s, n = map(int, input().split())

li = []

for i in range(n):
    li.append(tuple(map(int, input().split())))

li.sort()
defeat = False

for i in range(n):
    if s > li[i][0]:
        s += li[i][1]
        defeat = False
    else:
        defeat = True
        break


if defeat:
    print("NO")
else:
    print("YES")