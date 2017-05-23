# http://codeforces.com/problemset/problem/4/A

w = int(input())

if w<=2 or w%2!=0:
  print("NO")
else:
  print("YES")
  # for i in range(2, int(w/2), 2):
  #   if w-i % 2 == 0:
  #     print("YES")
  #     break