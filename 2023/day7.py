import functools
import sys
from collections import Counter

card_to_int_dict = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E'
}


def hand_to_hex(hand):
    hex_card = ""

    for card in hand[1]:
        hex_card += card_to_int_dict[card]

    return hand[0], int(hex_card, 16), hand[2]


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        lines = [
            [
                idx,
                line.split()[0],
                int(line.split()[1])
            ]
            for idx, line in enumerate(f.readlines())
        ]

    hex_lines = list()
    for line in lines:
        hex_lines.append(hand_to_hex(line))

    
    print(hex_lines)


    # lines.sort(key=functools.cmp_to_key([hand for _, hand, bet in lines]))
    print(lines)

    return 0


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return 0


def test_part_1():
    return_value = process_part_1('day7_tests.txt')
    if return_value != 6440:
        print(f'[test part1] expected 6440 got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part1] {return_value}')


def test_part_2():
    pass


def part_1():
    # print(f"[part1] {process_part_1('day7.txt')}")
    pass


def part_2():
    pass


test_part_1()
test_part_2()
part_1()
part_2()
