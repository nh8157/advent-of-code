def add_adjacent_number(number, number_pos, symbols):
    for i in range(-1, 2):
        for j in range(-1, len(number) + 1):
            if (number_pos[0] + i, number_pos[1] + j) in symbols:
                symbols[(number_pos[0] + i, number_pos[1] + j)].append(number)
    return symbols


def parse_input(schematic):
    numbers = {}
    symbols = {}
    
    for line_num in range(len(schematic)):
        line = schematic[line_num].strip("\n")
        i = 0
        while i < len(line):
            if line[i].isnumeric():
                j = i
                while j < len(line) and line[j].isnumeric():
                    j += 1
                numbers[(line_num, i)] = line[i:j]
                i = j
            else:
                if line[i] == "*":
                    symbols[(line_num, i)] = []
                i += 1
    return numbers, symbols

def get_sum(file):
    lines = open(file, "r").readlines()
    numbers, symbols = parse_input(lines)

    sum = 0
    for pos, num in numbers.items():
        add_adjacent_number(num, pos, symbols)
        
    for v in symbols.values():
        if len(v) == 2:
            sum += int(v[0]) * int(v[1])
    return sum

if __name__ == "__main__":
    file = "input_1.txt"
    print(get_sum(file))
