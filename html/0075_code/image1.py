a = 10
b = 10

def function():
  a = 20
  global b
  b = 20

print('before: a = ' + str(a)) # 10
print('before: b = ' + str(b)) # 10
function()
print('after: a = ' + str(a))  # 10
print('after: b = ' + str(b))  # 20
