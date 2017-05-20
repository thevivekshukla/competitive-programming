# http://codeforces.com/problemset/problem/231/A

n = int(input())

count = 0

for i in range(n):
  li = list(map(int, input().split()))

  one_counter = 0
  
  for j in li:
    if j == 1:
      one_counter += 1
      # print(one_counter)
  if one_counter >=2:
    count+=1
    # print("count", count)

print(count)