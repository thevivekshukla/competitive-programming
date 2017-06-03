# http://codeforces.com/problemset/problem/271/A

def is_distinct(s):
  s_list = list(s)
  s_set = set(s_list)

  if len(s_list) == len(s_set):
    return True
  else:
    return False

year = int(input())

for i in range(1, 9001):

  year += 1

  if is_distinct(str(year)):
    print(year)
    break

