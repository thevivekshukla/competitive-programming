# http://codeforces.com/problemset/problem/282/A

n = int(input())

value = 0

for i in range(n):
  c = input()

  if c[1] == '+':
    value += 1
  else:
    value -= 1


print(value)



