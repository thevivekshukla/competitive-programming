# http://codeforces.com/problemset/problem/133/A

s = input()

li = ["H", "Q", "9"]

flag = True

for i in li:
  if i in s:
    print("YES")
    flag = False
    break



if flag:
  print("NO")