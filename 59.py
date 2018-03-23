# http://codeforces.com/problemset/problem/510/A


n, m = map(int, input().split())


for row in range(1, n+1):
    row_even = (row % 2 == 0)
    row_odd = (row % 2 != 0)
    right_switch = (row % 4 != 0)    
    
    for col in range(1, m+1):
        
        if col == m and right_switch and row_even:
            print("#", end="")
            # right_switch = False
        elif col == 1 and not right_switch and row_even:
            print("#", end="")
            # right_switch = True
        elif row_even:
            print(".", end="")
        elif row_odd:
            print("#", end="")
        
    print()