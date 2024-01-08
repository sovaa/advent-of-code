import math
import sys
from pprint import pprint


class Node:
    west = None
    east = None
    north = None
    south = None

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


pipes = ['|', '-', 'L', 'J', '7', 'F', 'S']

can_go = {
    'east': {'S', '-', 'L', 'F'},
    'west': {'S', '-', 'J', '7'},
    'north': {'S', '|', 'L', 'J'},
    'south': {'S', '|', '7', 'F'}
}


def opposite(direction):
    if direction == 'east':
        return 'west'
    elif direction == 'west':
        return 'east'
    elif direction == 'north':
        return 'south'
    elif direction == 'south':
        return 'north'


def connects(chart, visited, row, col, direction):
    if chart[row][col] == '.':
        return False

    if direction == 'east' and col < len(chart[row]) - 1:
        if (row, col+1) in visited[-2:-1]:
            return False
        return chart[row][col+1] in can_go[opposite(direction)] and chart[row][col] in can_go[direction]

    elif direction == 'west' and col > 0:
        if (row, col-1) in visited[-2:-1]:
            return False
        return chart[row][col-1] in can_go[opposite(direction)] and chart[row][col] in can_go[direction]

    elif direction == 'north' and row > 0:
        if (row-1, col) in visited[-2:-1]:
            return False
        return chart[row-1][col] in can_go[opposite(direction)] and chart[row][col] in can_go[direction]

    elif direction == 'south' and row < len(chart) - 1:
        if (row+1, col) in visited[-2:-1]:
            return False
        return chart[row+1][col] in can_go[opposite(direction)] and chart[row][col] in can_go[direction]

    return False


def found_start(chart, row, col):
    return chart[row][col] == 'S'


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        chart = [line.replace("\n", "") for line in f.readlines()]

    start_row = -1
    start_col = -1

    for row, line in enumerate(chart):
        if 'S' in line:
            start_col = line.index('S')
            start_row = row

    graph = Node(start_row, start_col, 'S')

    cur_node = graph
    cur_row, cur_col = start_row, start_col
    visited = list()

    while True:
        visited.append((cur_row, cur_col))

        if connects(chart, visited, cur_row, cur_col, 'east'):
            cur_node.east = Node(cur_row, cur_col+1, chart[cur_row][cur_col+1])
            cur_col += 1
            cur_node = cur_node.east

            if found_start(chart, cur_row, cur_col):
                graph.west = cur_node
                break

        elif connects(chart, visited, cur_row, cur_col, 'west'):
            cur_node.west = Node(cur_row, cur_col-1, chart[cur_row][cur_col-1])
            cur_col -= 1
            cur_node = cur_node.west

            if found_start(chart, cur_row, cur_col):
                graph.south = cur_node
                break

        elif connects(chart, visited, cur_row, cur_col, 'south'):
            cur_node.south = Node(cur_row+1, cur_col, chart[cur_row+1][cur_col])
            cur_row += 1
            cur_node = cur_node.south

            if found_start(chart, cur_row, cur_col):
                graph.south = cur_node
                break

        elif connects(chart, visited, cur_row, cur_col, 'north'):
            cur_node.north = Node(cur_row-1, cur_col, chart[cur_row-1][cur_col])
            cur_row -= 1
            cur_node = cur_node.north

            if found_start(chart, cur_row, cur_col):
                graph.south = cur_node
                break

        else:
            raise Exception(f"Can't go anywhere from {cur_row}, {cur_col}")

    return math.ceil(len(visited) / 2)


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        series = [[int(number) for number in line.replace("\n", "").split()] for line in f.readlines()]


def test_part_1():
    return_value = process_part_1('day10_tests1.txt')
    if return_value != 4:
        print(f'[test part1] expected 4 got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part1] {return_value}')

    return_value = process_part_1('day10_tests2.txt')
    if return_value != 8:
        print(f'[test part1] expected 8 got {return_value}')
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
