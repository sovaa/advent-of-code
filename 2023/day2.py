import sys
import math


max_cubes_per_color = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def check_game_set(game_set):
    cubes = game_set.split(',')
    cube_sets = [cube.strip() for cube in cubes]
    set_results = list()

    for cube_set in cube_sets:
        n_cubes, color = cube_set.split()

        if color not in max_cubes_per_color:
            return False

        set_results.append(int(n_cubes) <= max_cubes_per_color[color])

    return all(set_results)


def check_file_p1(file_name):
    games = list()

    with open(file_name, 'r') as f:
        for line in f:
            game_id, results = line.split(':')
            game_id = game_id.replace('Game ', '')
            results = results.replace('\n', '')
            game_sets = results.split(';')
            all_games_passed = True

            for game_set in game_sets:
                if not check_game_set(game_set):
                    all_games_passed = False
                    break

            if all_games_passed:
                games.append(int(game_id))

    return sum(games)


def get_power_for_game(game_sets):
    color_to_number = dict()

    for game_set in game_sets:
        for cubes_and_color in game_set.split(','):
            cubes_and_color = cubes_and_color.strip()

            n_cubes, color = cubes_and_color.split()
            n_cubes = int(n_cubes)

            if color not in color_to_number or color_to_number[color] < n_cubes:
                color_to_number[color] = n_cubes

    return math.prod(color_to_number.values())


def check_file_p2(file_name):
    games = list()

    with open(file_name, 'r') as f:
        for line in f:
            _, results = line.split(':')
            results = results.replace('\n', '')
            game_sets = results.split(';')

            power = get_power_for_game(game_sets)
            games.append(int(power))

    return sum(games)


def test_part_1():
    result = check_file_p1('day2_tests.txt')
    if result != 8:
        print(f'expected 8 got {result}')
        sys.exit(1)


def test_part_2():
    result = check_file_p2('day2_tests.txt')
    if result != 2286:
        print(f'expected 2286 got {result}')
        sys.exit(1)


def part_1():
    print(check_file_p1('day2.txt'))


def part_2():
    print(check_file_p2('day2.txt'))


test_part_1()
test_part_2()

part_2()
