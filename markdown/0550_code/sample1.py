text = 'hello world'
d = {}

for c in text:
  if c in d:
    count = d[c]
    d[c] = count + 1
  else:
    d[c] = 1

print(d)
