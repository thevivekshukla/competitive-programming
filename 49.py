# http://codeforces.com/problemset/problem/59/A


s = input()

length = len(s)
up_count = 0

for i in s:
	if i.isupper():
		up_count += 1


if up_count > length//2:
	print(s.upper())
else:
	print(s.lower())