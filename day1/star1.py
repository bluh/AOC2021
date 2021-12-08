fd = open('./input.txt')

prev = 0
counter = 1

for line in fd:
    if prev == 0:
        prev = line
    else:
        if prev < line:
            print('increase from', prev, 'to', line)
            counter += 1
        prev = line

print('total', counter)
