import sys


def next_diff(history):
    return [history[i+1] - history[i] for i in range(len(history) - 1)]


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        series = [[int(number) for number in line.replace("\n", "").split()] for line in f.readlines()]

    predictions = list()

    for history in series:
        total = -1
        sub_series = [history]

        while total != 0:
            history = next_diff(history)
            total = sum(history)
            sub_series.append(history)

        sub_series[-1].append(0)
        for i in list(range(len(sub_series) - 1))[::-1]:
            sub_series[i].append(sub_series[i][-1] + sub_series[i+1][-1])

        predictions.append(sub_series[0][-1])

    return sum(predictions)


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        series = [[int(number) for number in line.replace("\n", "").split()] for line in f.readlines()]

    predictions = list()

    for history in series:
        total = -1
        sub_series = [history]

        while total != 0:
            history = next_diff(history)
            total = sum(history)
            sub_series.append(history)

        sub_series[-1] = [0] + sub_series[-1]
        for i in list(range(len(sub_series) - 1))[::-1]:
            sub_series[i] = [sub_series[i][0] - sub_series[i+1][0]] + sub_series[i]

        predictions.append(sub_series[0][0])

    return sum(predictions)


def test_part_1():
    return_value = process_part_1('day9_tests.txt')
    if return_value != 114:
        print(f'[test part1] expected 114 got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part1] {return_value}')


def test_part_2():
    return_value = process_part_2('day9_tests.txt')
    if return_value != 2:
        print(f'[test part2] expected 2 got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part2] {return_value}')


def part_1():
    result = process_part_1('day9.txt')
    print(f"[part1] {result}")


def part_2():
    result = process_part_2('day9.txt')
    print(f"[part2] {result}")


test_part_1()
test_part_2()
part_1()
part_2()
