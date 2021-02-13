text = input()
t1 = text[0:1]
t2 = text[1:2]
t3 = text[2:3]
 
if t1 == t2 and t1 == t3:
  print('Won')
else:
  print('Lost')