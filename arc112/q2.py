B, C = map(int, input().split())

num = B - C

if B == 0:
    print(C)
elif num < 0 and B < 0:
    print((C*2)+((-1*B)-C))
elif num < 0 and B > 0:
    print((C*2)+(B-C))
else:
    print(C*2-1)