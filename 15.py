# http://codeforces.com/problemset/problem/131/A

s = input()

if s[0].islower() and s[1:].isupper():
  print(s.capitalize())
elif s.isupper():
  print(s.lower())
elif len(s)==1 and s.islower():
  print(s.upper())
else:
  print(s)