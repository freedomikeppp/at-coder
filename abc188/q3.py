# ToDo: TLE
N = int(input())
l = list(map(int, input().split()))
input_list = []

for rate in l:
  input_list.append({'n': l.index(rate)+1, 'r': rate})

def get_winner(store):
  return_list = []
  for i in range(int(len(store)/2)):
    if store[2*i].get('r') < store[2*i+1].get('r'):
      return_list.append(store[2*i+1])
    else:
      return_list.append(store[2*i])
  return return_list

while len(input_list) != 2:
  input_list = get_winner(input_list)
  
if input_list[0].get('r') < input_list[1].get('r'):
  print(input_list[0].get('n'))
else:
  print(input_list[1].get('n'))
  