a = [1,2,3,4,5,6,7,8,9,10]

for i in a:
  print(i)
  if i % 2 == 0:
    print('fizz')
  elif i % 3 == 0:
    print('buzz')
  elif i % 6 == 0:
    print('fizzbuzz')
  print('----')
