# http://codeforces.com/contest/961/problem/A


n, m = map(int, input().split())

lim = list(map(int, input().split()))

dicn = dict()


for i in range(1, n+1):

    dicn[i] = lim.count(i)


print(min(dicn.values()))