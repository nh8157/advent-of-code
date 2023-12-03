def str_num(s):
    d = {"one": 1,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9}
    if s in d:
        return d[s]
    return None


def get_line_sum(line):
    sum = 0
    if len(line) == 0:
        return sum

    left_num = -1
    right_num = -1

    for i in range(len(line)):
        if line[i].isnumeric():
            right_num = int(line[i])
            if left_num == -1:
                left_num = right_num
            continue
        for j in range(3, 6):
            if i + j > len(line):
                break
            num = str_num(line[i : i+j])
            if num != None:
                right_num = num
                if left_num == -1:
                    left_num = num
                break

    if left_num >= 0 and right_num >= 0:
        sum = str(left_num) + str(right_num)
    return int(sum)


def get_file_sum(file):
    sum = 0
    lines = open(file, "r").readlines()
    for line in lines:
        sum += get_line_sum(line)
    return sum


if __name__ == '__main__':
    # print(get_line_sum("zoneight234"))
    file = "input_2.txt"
    print(get_file_sum(file))
