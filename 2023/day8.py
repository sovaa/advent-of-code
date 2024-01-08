from functools import reduce
import math


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        lines = [line.replace("\n", "") for line in f.readlines()]

    """
    RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)
    """

    instructions = lines[0]
    steps = lines[2:]

    nodes = dict()

    for step in steps:
        name, children = step.split(' = ')
        children = children[1:-1].split(', ')

        if name in nodes:
            raise Exception(f"Node {name} already exists")

        nodes[name] = children

    current_node = 'AAA'
    n_steps_taken = 0

    while current_node != 'ZZZ':
        for instruction in instructions:
            if instruction == 'L':
                current_node = nodes[current_node][0]
            elif instruction == 'R':
                current_node = nodes[current_node][1]
            else:
                raise Exception(f"Unknown instruction {instruction}")

            n_steps_taken += 1

    return n_steps_taken


def get_periods(instructions, steps):
    nodes = dict()

    for step in steps:
        name, children = step.split(' = ')
        children = children[1:-1].split(', ')
        nodes[name] = children

    current_nodes = [node for node in nodes.keys() if node.endswith('A')]
    periods = [[current_node] for current_node in current_nodes]
    n_steps_taken = 0

    while True:
        for instruction in instructions:
            n_steps_taken += 1

            for node_idx, current_node in enumerate(current_nodes):
                if instruction == 'L':
                    current_nodes[node_idx] = nodes[current_node][0]
                elif instruction == 'R':
                    current_nodes[node_idx] = nodes[current_node][1]
                else:
                    raise Exception(f"Unknown instruction {instruction}")

                if current_nodes[node_idx].endswith('Z'):
                    periods[node_idx].append(n_steps_taken)

            if all((len(period) >= 2 for period in periods)):
                return [p[1] for p in periods]


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        lines = [line.replace("\n", "") for line in f.readlines()]

    instructions = lines[0]
    steps = lines[2:]

    periods = get_periods(instructions, steps)
    lcm = math.lcm(*periods)

    return lcm


def test_part_1():
    return_value = process_part_1('day8_tests1.txt')
    if return_value != 2:
        print(f'[test part1 1/2] expected 2 got {return_value}')
        # sys.exit(1)
    else:
        print(f'[test part1 1/2] {return_value}')

    return_value = process_part_1('day8_tests2.txt')
    if return_value != 6:
        print(f'[test part1 2/2] expected 6 got {return_value}')
        # sys.exit(1)
    else:
        print(f'[test part1 2/2] {return_value}')


def test_part_2():
    return_value = process_part_2('day8_tests_part2.txt')
    if return_value != 6:
        print(f'[test part1 2/2] expected 6 got {return_value}')
        # sys.exit(1)
    else:
        print(f'[test part1 2/2] {return_value}')


def part_1():
    result = process_part_1('day8.txt')
    assert result == 20513
    print(f"[part1] {result}")


def part_2():
    result = process_part_2('day8.txt')
    assert result < 5448913399014485733178768440
    assert result < 147858713687432582970389100
    assert result < 95971002323538
    assert result == 15995167053923
    print(f"[part2] {result}")


test_part_1()
test_part_2()
part_1()
part_2()
