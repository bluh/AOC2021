h = 0
d = 0
a = 0

for line in open('./input.txt'):
  split = line.split(' ')
  dir = split[0]
  amt = int(split[1])
  if dir == 'up':
    a -= amt
  elif dir == 'down':
    a += amt
  elif dir == 'forward':
    h += amt
    d += (a * amt)


print('h', h, 'd', d, 'total', h*d)