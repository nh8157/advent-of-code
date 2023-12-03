def get_min_combination(game):
    combination = {"red": None, "green": None, "blue": None}
    for reveal in game:
        for k, v in reveal.items():
            if combination[k] == None or combination[k] < v:
                combination[k] = v
    return combination


def parse_reveal(reveal):
    parsed = {}
    r = reveal.split(", ")
    for draw in r:
        info = draw.split(" ")
        num = int(info[0])
        color = info[1]
        parsed[color] = num
    return parsed


def parse_game(game):
    parsed = []
    reveals = game.split("; ")
    for r in reveals:
        parsed.append(parse_reveal(r))
    return parsed


def get_impossible_game_ids(file):
    # open file
    lines = open(file, "r").readlines()
    
    sum = 0
    for line in lines:
        line = line.strip("\n")
        game = line.split(": ")
        game_content = game[1]
        
        power = 1
        combination = get_min_combination(parse_game(game_content))
        for num in combination.values():
            if num != None:
                power *= num
            else:
                power *= 0
        sum += power
    return sum


if __name__ == "__main__":
    file = "input_1.txt"
    print(get_impossible_game_ids(file))