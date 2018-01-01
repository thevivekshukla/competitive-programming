# http://codeforces.com/problemset/problem/268/A

n = int(input())

li = []

for i in range(n):
	t = tuple(map(int, input().split()))
	li.append(t)


# print(li)

# h_li, g_li = zip(*li)

# print(h_li)
# print(g_li)

# for i in range(len(li)):
# 	print(i, li[i])

h = 0
g = 1
count = 0


for i in range(n):
	for j in range(n):
		if i != j and li[i][h] == li[j][g]:
			count += 1


print(count)