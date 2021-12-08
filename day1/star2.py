fd = open('./input.txt')

window = [0, 0, 0]
queue = 0
prev = 0
counter = 1

for line in fd:
    if queue < 3:
        window[queue] = int(line)
        queue += 1
    elif queue == 3:
        prev = window[0] + window[1] + window[2]
        queue = 4
    else:
        window.pop(0)
        window.append(int(line))
        total = window[0] + window[1] + window[2]
        if prev == 0:
            prev = total
        else:
            print('comparing', prev, total)
            if prev < total:
                counter += 1
            prev = total


print('total', counter)
