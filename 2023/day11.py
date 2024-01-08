import math
import sys
from pprint import pprint


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        chart = [line.replace("\n", "") for line in f.readlines()]

    rows_to_expand = list()
    cols_to_expand = list()

    expanded_cols = [""] * len(chart)
    expanded_chart = list()

    for line in chart:
        print(line)

    for row_nr, row in enumerate(chart):
        if all((c == '.' for c in row)):
            rows_to_expand.append(row_nr)

    for col_nr in range(len(chart[0])):
        all_empty = True
        for row_nr, row in enumerate(chart):
            if row[col_nr] != '.':
                all_empty = False
                break

        if all_empty:
            cols_to_expand.append(col_nr)

    for row_nr, row in enumerate(chart):
        for col_nr in range(len(row)):
            expanded_cols[row_nr] += chart[row_nr][col_nr]
            if col_nr in cols_to_expand:
                expanded_cols[row_nr] += chart[row_nr][col_nr]

    for row_nr, row in enumerate(expanded_cols):
        expanded_chart.append(row)
        if row_nr in rows_to_expand:
            expanded_chart.append(row)

    print()
    for line in expanded_chart:
        print(line)


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        series = [[int(number) for number in line.replace("\n", "").split()] for line in f.readlines()]


def test_part_1():
    return_value = process_part_1('day11_tests.txt')
    if return_value != 374:
        print(f'[test part1] expected 374 got {return_value}')
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
    result = process_part_1('day10.txt')
    print(f"[part1] {result}")


def part_2():
    result = process_part_2('day10.txt')
    print(f"[part2] {result}")


test_part_1()
# test_part_2()
part_1()
# part_2()
