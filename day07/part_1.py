from functools import cmp_to_key

def parse_hand(hand):
    hand_to_int_map = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10
    }
    nums = []
    for n in hand:
        if n.isnumeric():
            nums.append(int(n))
        else:
            nums.append(hand_to_int_map[n])
    return nums

def find_type(bid):
    m = {}
    freq_m = {}
    for n in bid:
        if n not in m.keys():
            m[n] = 0
        m[n] += 1
    for freq in m.values():
        if freq not in freq_m.keys():
            freq_m[freq] = 0
        freq_m[freq] += 1
    if 5 in freq_m.keys():
        return 7
    elif 4 in freq_m.keys():
        return 6
    elif 3 in freq_m.keys():
        if 2 in freq_m.keys():
            return 5
        return 4
    elif 2 in freq_m.keys():
        if freq_m[2] == 2:
            return 3
        return 2
    return 1

def comparator_wrapper(x, y):
    return comparator(x[0], y[0])

def comparator(x, y):
    x_type = find_type(x)
    y_type = find_type(y)
    if x_type < y_type:
        return -1
    elif x_type > y_type:
        return 1
    for i in range(len(x)):
        if x[i] < y[i]:
            return -1
        elif x[i] > y[i]:
            return 1
    return 1

if __name__ == "__main__":
    f = open("input.txt", "r")
    bids = []
    amount = 0
    for l in f.readlines():
        # parse and process the lines
        hand = parse_hand(l.split()[0])
        bid = int(l.split()[1])
        bids.append([hand, bid])
    # order the bids according to the hand
    bids.sort(key=cmp_to_key(comparator_wrapper))
    # calculate the winning amount
    for i in range(len(bids)):
        amount += bids[i][1] * (i + 1)
    print(amount)