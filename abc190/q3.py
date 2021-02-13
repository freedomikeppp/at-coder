N, M = map(int, input().split())
l = []
r = []

for _ in range(M):
  A, B = map(int, input().split())
  l.append((A,B))

K = int(input())

for k in range(K):
  C, D = map(int, input().split())
  r.append((C,D))

