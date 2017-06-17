# http://codeforces.com/problemset/problem/469/A

n = int(input())

li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

li1.pop(0)
li2.pop(0)

li1.extend(li2)

s = set(li1)

if len(s)==n:
  print("I become the guy.")
else:
  print("Oh, my keyboard!")