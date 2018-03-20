# http://codeforces.com/contest/926/problem/A


l, r = tuple(map(int, input().split()))

import math

result = 0


for i in range(l, r+1):
    x = math.log(i, 2)
    y = math.log(i, 3)

    if not (x > int(x)) or not (y > int(y)):
        result += 1

print(result)