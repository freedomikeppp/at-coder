A, B, C = map(int, input().split())

if C == 0:
  if A <= B:
    print('Aoki')
  else:
    print('Takahashi')
else:
  if B <= A:
    print('Takahashi')
  else:
    print('Aoki')

# Best answer
A, B, C = map(int, input().split())
if A + C > B:
    print("Takahashi")
else:
    print("Aoki")