import re
from math import floor, ceil

pattern = r'\d+'

def find_numbers(s):
    numbers = re.findall(pattern, s)
    num_str = "".join(numbers)
    return int(num_str)

def get_combi(time, distance):
    print("time:", time, "distance:", distance)
    left = ceil((time - (time ** 2 - 4 * distance) ** 0.5) / 2)
    right = floor((time + (time ** 2 - 4 * distance) ** 0.5) / 2)
    if (time - left) * left == distance:
        left += 1
    if (time - right) * right == distance:
        right -= 1
    return right - left + 1

if __name__ == "__main__":
    f = open("input.txt", "r")
    time = find_numbers(f.readline())
    distance = find_numbers(f.readline())
    prod = 1
    combi = get_combi(time, distance)
    if combi > 0:
        prod *= combi
    print(prod)