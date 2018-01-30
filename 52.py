# http://codeforces.com/problemset/problem/443/A

st = input()

if st == '{}':
	print(0)
else:
	st_li = st[1:-1].split(", ")
	print(len(set(st_li)))