# http://codeforces.com/problemset/problem/236/A

s = input()

li = []

for i in range(len(s)):
  li.append(s[i])

li = list(set(li))


if len(li)%2==0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")