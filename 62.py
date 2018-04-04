# http://codeforces.com/problemset/problem/339/B


n, m = map(int, input().split())
li_m = list(map(int, input().split()))

time = 0


for i in range(m):

    if time == 0:
        time += li_m[i] - 1
        ptr = li_m[i]
    elif ptr > li_m[i]:
        time += n - ptr + li_m[i]
        ptr = li_m[i]
    else:
        time += li_m[i] - ptr
        ptr = li_m[i]


print(time)