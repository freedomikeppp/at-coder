N, X = map(int, input().split())
drunk_ml = 0

for i in range(N):
  V, P = map(int, input().split())
  drunk_ml += V*P
  if drunk_ml > X*100:
    print(i+1)
    exit()

print(-1)