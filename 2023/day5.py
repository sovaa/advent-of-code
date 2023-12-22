import sys


def check_file_p1(file_name):
    return 0


def check_file_p2(file_name):
    return 0


def test_part_1():
    return_value = check_file_p1('day5_tests.txt')
    if return_value != 35:
        print(f'[part1] expected 35 got {return_value}')
        sys.exit(1)


def test_part_2():
    return_value = check_file_p2('day5_tests.txt')
    if return_value != 30:
        print(f'[part2] expected 30 got {return_value}')
        sys.exit(1)


def part_1():
    print(f"[part1] {check_file_p1('day5.txt')}")


def part_2():
    print(f"[part2] {check_file_p2('day5.txt')}")


test_part_1()
# test_part_2()
# part_1()
# part_2()
