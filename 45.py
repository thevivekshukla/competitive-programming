# http://codeforces.com/problemset/problem/61/A

one = input()
two = input()

res = ''

l = len(one)

for i in range(l):
  if one[i] == two[i]:
    res += '0'
  else:
    res += '1'


print(res)