V, T, S, D = map(int, input().split())
need_time = D / V

if T <= need_time and need_time <= S:
    print('No')
else:
    print('Yes')