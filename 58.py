# http://codeforces.com/problemset/problem/520/A


n = int(input())
s = set(input().lower())


if len(s) == 26:
    print("YES")
else:
    print("NO")