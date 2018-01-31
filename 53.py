# http://codeforces.com/problemset/problem/500/A

n, t = tuple(map(int, input().split()))
a = list(map(int, input().split()))

i = 1

for j in range(1, n):

	if t == 1:
		print("YES")
		break
	else:
		temp = i + a[i-1]
		i = temp
		if t == i:
			print("YES")
			break
		elif i > n-1:
			print("NO")
			break
