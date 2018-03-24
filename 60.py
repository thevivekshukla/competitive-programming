# http://codeforces.com/problemset/problem/141/A


names = list(input()) + list(input())
mix = list(input())

names.sort()
mix.sort()


if len(names) == len(mix):
    if names == mix:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

