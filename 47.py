# http://codeforces.com/problemset/problem/344/A

n = int(input())

prev = input()

group = 1

for i in range(n-1):

  m = input()

  if prev != m:
    group+=1

  prev = m


print(group)