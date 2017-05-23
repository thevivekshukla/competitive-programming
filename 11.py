# http://codeforces.com/problemset/problem/339/A

s = input()

one = 0
two = 0
three = 0

if len(s)==1:
  print(s)
else:
  for i in range(len(s)):
    if s[i] == '1':
      one+=1
    elif s[i] == '2':
      two+=1
    elif s[i] == '3':
      three+=1

  s2 = ""

  for i in range(one):
    s2 += '1+'
  for i in range(two):
    s2 += '2+'
  for i in range(three):
    s2 += '3+'

  s2 = s2.strip('+')

  print(s2)