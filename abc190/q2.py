N, S, D = map(int, input().split())
X_list = []
Y_list = []

for i in range(N):
  X, Y = map(int, input().split())
  if X >= S:
    continue
  elif Y <= D:
    continue
  X_list.append(X)
  Y_list.append(Y)

if len(X_list) > 0:
  print('Yes')
else:
  print('No')

# Best answer
N, S, D = map(int, input().split())
def check():
    X, Y = map(int, input().split())
    return X < S and Y > D

if any(check() for i in range(N)):
    print("Yes")
else:
    print("No")
