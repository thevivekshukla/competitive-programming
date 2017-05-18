# http://codeforces.com/problemset/problem/118/A


s = input()

s = s.lower()

vowels = ['a', 'o', 'y', 'e', 'u', 'i']

for i in vowels:
  if i in s:
    s = s.replace(i, '')
    

st = ""

for i in range(len(s)):
  st += s[i].replace(s[i], '.'+s[i])

print(st)
