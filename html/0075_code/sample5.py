a = 5

def function():
  global a
  a = 10
  print('function(): ' + str(a))

print('global: ' + str(a))
function()
print('global: ' + str(a))
