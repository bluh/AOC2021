h = 0
d = 0

for line in open('./input.txt'):
  split = line.split(' ')
  dir = split[0]
  amt = int(split[1])
  if dir == 'up':
    d -= amt
  elif dir == 'down':
    d += amt
  elif dir == 'forward':
    h += amt


print('h', h, 'd', d, 'total', h*d)