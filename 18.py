# http://codeforces.com/problemset/problem/160/A


n = int(input())

li = list(map(int, input().split()))

li.sort(reverse=True)

count = 0

for i in range(n):
  if sum(li[:i+1]) > sum(li[i+1:]):
    count = i+1
    break


print(count)