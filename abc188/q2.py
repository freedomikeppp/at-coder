n = int(input())
list_a = list(input().split())
list_b = list(input().split())

r = 0

for i in range(n):
  r += int(list_a[i]) * int(list_b[i])

print("Yes" if r == 0 else "No")