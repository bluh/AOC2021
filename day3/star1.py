zeros = []
ones = []
init = False

for line in open('input.txt'):
    if not init:
        zeros = [0] * (len(line) - 1)
        ones = [0] * (len(line) - 1)
        init = True
    # print('looking at', line, 'with', zeros, ones)
    for index, char in enumerate(line):
        # print('\tconsuming', index, char)
        if char == '0':
            zeros[index] += 1
        elif char == '1':
            ones[index] += 1

print(zeros)
print(ones)

gamma = 0
epsilon = 0

for index in range(len(zeros)):
    gamma = gamma << 1
    epsilon = epsilon << 1
    if zeros[index] < ones[index]:
        gamma += 1
    else:
        epsilon += 1

print('final', gamma, epsilon, gamma * epsilon)
