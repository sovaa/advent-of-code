import sys
import math


def distance_for_hold_time(hold_time, max_time_allowed):
    return hold_time * (max_time_allowed - hold_time)


def hold_time_for_distance(dist, max_time, calculate_max: bool = True):
    """
    all races are quadratic in nature:
      distance = hold_time * (max_time - hold_time)

    solving for hold_time using the quadratic formula:
      hold_time = (-b +/- sqrt(b^2 - 4ac)) / 2a

    :param calculate_max if True, calculate the max time (positive square root), otherwise
        calculate the min time (negative square root)
    """
    mod = 1 if calculate_max else -1

    return (max_time + mod * math.sqrt(max_time ** 2 - 4 * dist)) / 2


def process_races(times, distances):
    ways_to_win = list()

    for time, distance in zip(times, distances):
        # find max and min value of hold time to get the record
        hold_time_max = hold_time_for_distance(distance, time, True)
        hold_time_min = hold_time_for_distance(distance, time, False)

        # have to be over the min
        needed_to_win_min = math.ceil(hold_time_min)
        if needed_to_win_min == math.floor(hold_time_min):
            needed_to_win_min += 1

        # ...and under the max
        needed_to_win_max = math.floor(hold_time_max)
        if needed_to_win_max == math.ceil(hold_time_max):
            needed_to_win_max -= 1

        ways_to_win.append(needed_to_win_max - needed_to_win_min + 1)

    return math.prod(ways_to_win)


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    times = [int(t) for t in lines[0].split(":")[1].strip().split()]
    distances = [int(d) for d in lines[1].split(":")[1].strip().split()]

    return process_races(times, distances)


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    # combines the numbers into one so we get:
    #   Time: 71530
    #   Distance: 940200
    times = [int(lines[0].split(":")[1].strip().replace(' ', ''))]
    distances = [int(lines[1].split(":")[1].strip().replace(' ', ''))]

    return process_races(times, distances)


def test_part_1():
    return_value = process_part_1('day6_tests.txt')
    if return_value != 288:
        print(f'[test part1] expected 288 (4*8*9) got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part1] {return_value}')


def test_part_2():
    return_value = process_part_2('day6_tests.txt')
    if return_value != 71503:
        print(f'[test part2] expected 71503 got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part2] {return_value}')


def part_1():
    print(f"[part1] {process_part_1('day6.txt')}")


def part_2():
    print(f"[part2] {process_part_2('day6.txt')}")


test_part_1()
test_part_2()
part_1()
part_2()
