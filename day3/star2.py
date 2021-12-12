LINES = []
LENGTH = 12

for line in open('input.txt'):
    LINES.append(line.strip())

def generate_filter(at_index, expected):
    return lambda str: str[at_index] == expected

for index in range(LENGTH):
    if len(LINES) > 1:
        zeros = 0
        ones = 0
        for line in LINES:
            if line[index] == '0':
                zeros += 1
            elif line[index] == '1':
                ones += 1

        #to find the most occurring bit:
        #'0' if zeros > ones else '1'
        #to find the least occuring bit:
        #'0' if zeros <= ones else '1'
        LINES = list(filter(generate_filter(index, '0' if zeros <= ones else '1'), LINES))
        print('new lines', LINES)

print('stopped with', LINES, int(LINES[0], 2))
