H, W = map(int, input().split())
s_list = [['.']*H]*W


for i in range(H):
    l = input().split()
    print(l)
    for j in range(W):
        s_list[i][j] = l[j]

print(s_list)

