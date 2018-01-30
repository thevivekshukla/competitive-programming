# http://codeforces.com/problemset/problem/25/A


n = int(input())
nums = list(map(int, input().split()))

even_count = 0
odd_count = 0


for i in range(n):
	if nums[i]%2 == 0:
		even_count += 1
		even_index = i+1
	else:
		odd_count += 1
		odd_index = i+1

if even_count == n-1:
	print(odd_index)
else:
	print(even_index)
