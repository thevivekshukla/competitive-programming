# http://codeforces.com/problemset/problem/144/A

n = int(input())

li = list(map(int, input().split()))

mx = max(li)
mn = min(li)

in_mx = li.index(mx)
in_mn = 0

li.remove(mx)
li.insert(0, mx)



for i in li[::-1]:
  in_mn += 1
  if i==mn:
    in_mn = abs(n-in_mn)
    break


print(in_mx + abs(n-1-in_mn))