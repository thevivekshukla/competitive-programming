# http://codeforces.com/problemset/problem/467/A

n = int(input())

count = 0

for i in range(n):

  p, q = tuple(map(int, input().split()))

  if p+2<=q:
    count+=1


print(count)