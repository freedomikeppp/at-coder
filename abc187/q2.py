N = int(input())
p_list = []
count = 0

for _ in range(N):
  p_list.append(tuple(map(int, input().split())))
  
for i in range(N):
  b_point = p_list[i]
  for j in range((N-1)-i):
    e_point = p_list[(j+1)+i]
    slope = (e_point[1] - b_point[1]) / (e_point[0] - b_point[0])
    if slope <=1 and slope >= -1:
      count += 1
      
print(count)