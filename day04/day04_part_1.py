def count_to_points(n):
    if n <= 0:
        return 0
    return 2 ** (n - 1)

def get_nums(str_nums):
    s = set()
    nums = str_nums.split(" ")
    for n in nums:
        if n.isnumeric():
            s.add(int(n))
    return s

def get_winning_count(winning, actual):
    s = 0
    for i in actual:
        if i in winning:
            s += 1
    return s

def get_points(f):
    lines = open(f, "r").readlines()
    points = 0
    for line in lines:
        nums = line.split(": ")[1].strip("\n").split(" | ")
        winning = get_nums(nums[0])
        actual = get_nums(nums[1])
        c = get_winning_count(winning, actual)
        p = count_to_points(c)
        points += p
    return points

if __name__ == "__main__":
    file = "input_1.txt"
    print(get_points(file))
