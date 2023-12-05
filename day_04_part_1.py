def src_to_dst(m, src):
    for corr in m:
        if corr[1] <= src and corr[1] + corr[2] > src:
            return corr[0] + (src - corr[1])
    return src

def break_maps(lines):
    maps = []
    left = 0
    for right in range(len(lines)):
        if lines[right] == "\n":
            nums = [s.strip('\n').split() for s in lines[left + 1:right]]
            for i in range(len(nums)):
                nums[i] = [int(n) for n in nums[i]]
            maps.append(nums)
            left = right + 1
        elif right == len(lines) - 1:
            nums = [s.strip('\n').split() for s in lines[left + 1:right + 1]]
            for i in range(len(nums)):
                nums[i] = [int(n) for n in nums[i]]
            maps.append(nums)
    return maps

def get_min_location(file):
    file = "input_1.txt"
    lines = open(file, 'r').readlines()
    seeds = lines[0].split(": ")[1].split()
    maps = break_maps(lines[2:])

    min_loc = None
    for seed in seeds:
        src = int(seed)
        for m in maps:
            src = src_to_dst(m, src)
        if min_loc is None or min_loc > src:
            min_loc = src
    return min_loc

if __name__ == "__main__":
    file = "input_1.txt"
    print(get_min_location(file))
