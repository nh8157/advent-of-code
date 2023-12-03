def is_reveal_possible(expected, actual):
    for k, v in actual.items():
        if expected[k] < v:
            return False
    return True


def is_game_possible(expected, game):
    for g in game:
        if is_reveal_possible(expected, g):
            continue
        return False
    return True


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


def get_impossible_game_ids(expected, file):
    # open file
    lines = open(file, "r").readlines()
    
    sum = 0
    for line in lines:
        line = line.strip("\n")
        game = line.split(": ")
        game_id = int(game[0].split(" ")[1])
        game_content = game[1]
        
        if is_game_possible(expected, parse_game(game_content)):
            sum += game_id

    return sum


if __name__ == "__main__":
    file = "input_1.txt"
    expected = {"red": 12, "green": 13, "blue": 14}
    print(get_impossible_game_ids(expected, file))