N = 963761198400
i = 1
count = 0

while N >= i:
  # 奇数判定
  if N % i == 0:
    count += 1
    
    center_num = N / i
    if center_num - int(i/2) >= 0:
      count += 1
    
  # インクリメント
  i = i + 2
  
print(count)