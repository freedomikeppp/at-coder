N = int(input())
n_set = set()
e_set = set()

for _ in range(N):
  s = input()
  if s[0] != '!':
    if s[0:] in e_set:
      print(s[0:])
      exit()
    n_set.add(s[0:])
  else:
    if s[1:] in n_set:
      print(s[1:])
      exit()
    e_set.add(s[1:])

print(n_set)
print(e_set)
print('satisfiable')
