T = int(input())
 
for _ in range(T):
    L, R = map(int, input().split())
    
    if L == 0 and R == 0:
      print(1)
      continue
      
    num = R - (L + (L - 1))
    
    if num < 0:
      print(0)
      continue
      
    print(int(num * (num + 1) / 2))