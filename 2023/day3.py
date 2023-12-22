import sys
import re
import math


def is_symbol(c: str):
    if c.isdigit():
        return False
    if c == '.':
        return False
    return True


def line_has_symbols(line, start, end):
    start_idx = start - 1 if start - 1 >= 0 else 0
    end_idx = end + 1 if end + 1 <= len(line) else len(line)

    return any([is_symbol(c) for c in line[start_idx:end_idx]])


def line_has_numbers(line, start, end):
    start_idx = start - 1 if start - 1 >= 0 else 0
    end_idx = end + 1 if end + 1 <= len(line) else len(line)

    return any([c.isdigit() for c in line[start_idx:end_idx]])


def find_all_numbers_and_positions(lines):
    results = list()

    for row, line in enumerate(lines):
        for match in re.finditer('\d+', line):  # noqa: E605
            start = match.start()
            end = match.end()
            number = line[start:end]

            results.append((row, number, start, end))

    return results


def pos_for_first_non_digit(s):
    for idx, c in enumerate(s):
        if not c.isdigit():
            return idx
    return len(s)


def get_number_from_line(line, start):
    found_numbers = list()

    # iterate over all matches, since there could be two on one line, e.g.:
    #
    # ..667.778..
    # .....*.....
    for match in re.finditer('\d+', line):
        match_start = match.start()
        match_end = match.end()

        if start >= match_start - 1 and start <= match_end:
            found_numbers.append(int(line[match_start:match_end]))

    return found_numbers


def find_all_gears(lines):
    results = list()
    n_rows = len(lines)

    for row, line in enumerate(lines):
        for match in re.finditer('\*', line):  # noqa: E605
            numbers_for_gear = list()

            start = match.start()

            check_before = start > 0
            check_after = start + 1 < len(line)
            check_prev_line = row > 0
            check_next_line = row < n_rows - 1

            if check_before and line[start-1].isdigit():
                rev_position = pos_for_first_non_digit(list(reversed(line[:start])))
                number = line[start-rev_position:start]
                numbers_for_gear.append(int(number))

            if check_after and line[start+1].isdigit():
                position = pos_for_first_non_digit(line[start+1:])
                number = line[start+1:start+1+position]
                numbers_for_gear.append(int(number))

            if check_prev_line:
                prev_line = lines[row-1]
                if any((c.isdigit() for c in prev_line[start-1:start+2])):
                    numbers_for_gear.extend(get_number_from_line(prev_line, start))

            if check_next_line:
                next_line = lines[row+1]
                if any((c.isdigit() for c in next_line[start-1:start+2])):
                    numbers_for_gear.extend(get_number_from_line(next_line, start))

            if len(numbers_for_gear) >= 2:
                results.append(math.prod(numbers_for_gear))

    return sum(results)


def check_file_p1(file_name):
    with open(file_name, 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    n_rows = len(lines)

    numbers_and_pos = find_all_numbers_and_positions(lines)
    valid_numbers = list()

    for row_idx, number, start, end in numbers_and_pos:
        check_prev_line = row_idx > 0
        check_next_line = row_idx < n_rows - 1

        if check_prev_line:
            if line_has_symbols(lines[row_idx - 1], start, end):
                valid_numbers.append(number)
                continue

        if check_next_line:
            if line_has_symbols(lines[row_idx + 1], start, end):
                valid_numbers.append(number)
                continue

        if line_has_symbols(lines[row_idx], start, end):
            valid_numbers.append(number)
            continue

    return sum([int(number) for number in valid_numbers])


def check_file_p2(file_name):
    with open(file_name, 'r') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]

    return find_all_gears(lines)


def test_part_1():
    return_value = check_file_p1('day3_tests.txt')
    if return_value != 4361:
        print(f'expected 4361 got {return_value}')
        sys.exit(1)


def test_part_2():
    return_value = check_file_p2('day3_tests.txt')

    # if return_value != 2491504:  # tests3
    # if return_value != 15529473:  # tests2
    if return_value != 467835:  # tests
        print(f'expected 467835 got {return_value}')
        sys.exit(1)


def part_1():
    print(check_file_p1('day3.txt'))


def part_2():
    print(check_file_p2('day3.txt'))


test_part_1()
test_part_2()
part_1()
part_2()
