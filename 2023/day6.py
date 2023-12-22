import sys


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    times = [int(t) for t in lines[0].split(":")[1].strip().split()]
    distances = [int(d) for d in lines[1].split(":")[1].strip().split()]

    print(times)
    print(distances)

    

    return 0


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return 0


def test_part_1():
    return_value = process_part_1('day6_tests.txt')
    if return_value != 288:
        print(f'[part1] expected 288 (4*8*9) got {return_value}')
        sys.exit(1)


def test_part_2():
    pass


def part_1():
    print(f"[part1] {process_part_1('day5.txt')}")


def part_2():
    print(f"[part2] {process_part_2('day5.txt')}")


test_part_1()
test_part_2()
part_1()
part_2()
