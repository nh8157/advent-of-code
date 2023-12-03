def is_adjacent(number_len, number_pos, symbols):
    for i in range(-1, 2):
        for j in range(-1, number_len + 1):
            if (number_pos[0] + i, number_pos[1] + j) in symbols:
                return True
    return False


def parse_input(schematic):
    numbers = {}
    symbols = set()
    
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
                if line[i] != ".":
                    symbols.add((line_num, i))
                i += 1
    return numbers, symbols

def get_sum(file):
    lines = open(file, "r").readlines()
    numbers, symbols = parse_input(lines)

    sum = 0
    for pos, num in numbers.items():
        if is_adjacent(len(num), pos, symbols):
            sum += int(num)
    
    return sum

if __name__ == "__main__":
    file = "input_1.txt"
    print(get_sum(file))
