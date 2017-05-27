# http://codeforces.com/problemset/problem/58/A

import re

reg = re.compile(r'(h)+[a-z]*(e)+[a-z]*(l)+[a-z]*(l)+[a-z]*(o)+[a-z]*')

s1 = input()

li = reg.findall(s1)

if not li:
  print("NO")
else:
  print("YES")