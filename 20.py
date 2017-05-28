# http://codeforces.com/problemset/problem/122/A

n = int(input())

flag = False
not_lucky = False
s = str(n)

for i in range(len(s)):
  if s[i] == '4' or s[i] == '7':
    pass
  else:
    not_lucky = True
    break


if not not_lucky:
  flag = True

if flag:
  print("YES")
elif n%47 == 0:
  print("YES")
elif n%4 == 0:
  print("YES")
elif n%7 == 0:
  print("YES")
else:
  print("NO")