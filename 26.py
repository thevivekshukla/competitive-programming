# http://codeforces.com/problemset/problem/266/B

n, t = tuple(map(int, input().split()))

s = list(input())

li = []

for i in range(len(s)):
  if s[i] == 'B':
    li.append(i)


for j in range(t):

  for i in range(len(li)):
    try:
      if s[li[i]+1] == 'G':
        s[li[i]] = 'G'
        s[li[i]+1] = 'B'
        li[i] = li[i]+1
    except:
      pass


s = "".join(s)
print(str(s))