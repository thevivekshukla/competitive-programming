# http://codeforces.com/problemset/problem/734/A

n = int(input())
s = list(input())

a_count = s.count('A')
b_count = n - a_count

if a_count > b_count:
    print('Anton')
elif a_count == b_count:
    print('Friendship')
else:
    print('Danik')