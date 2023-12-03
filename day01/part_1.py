def get_line_sum(line):
    sum = 0
    if len(line) == 0:
        return sum

    left = -1
    right = -1
    
    for i in range(len(line)):
        if line[i].isnumeric():
            right = i
            if left == -1:
                left = right

    if left >= 0 and right >= 0:
        sum = int(line[left] + line[right])
    return sum

def get_file_sum(file):
    sum = 0
    lines = open(file, "r").readlines()
    for line in lines:
        sum += get_line_sum(line)
    return sum

if __name__ == '__main__':
    file = "input.txt"
    print(get_file_sum(file))