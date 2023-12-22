import queue
import sys
from collections import defaultdict
from pprint import pprint


def wins_for_card(winning_numbers, card_numbers):
    hits = 0

    for number in card_numbers:
        if number in winning_numbers:
            # print(f"card {idx} has winning number {number}")
            hits += 1

    return hits


def process_cards_in_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return [
        (
            set(int(card) for card in card_list[0].split()),
            [int(card) for card in card_list[1].split()]
        )
        for card_list in [line.split(':')[1].strip().split(' | ') for line in lines]
    ]


def check_file_p1(file_name):
    cards = process_cards_in_file(file_name)
    total_scores = 0

    for idx, (winning_numbers, card_numbers) in enumerate(cards):
        hits = wins_for_card(winning_numbers, card_numbers)

        if hits > 0:
            # print(f"card {idx} has {hits} hits, total score is {2**hits}")
            total_scores += 2**(hits-1)

    return total_scores


def check_file_p2(file_name):
    cards = process_cards_in_file(file_name)
    card_id_to_numbers = [
        (idx, winning_numbers, card_numbers)
        for idx, (winning_numbers, card_numbers) in enumerate(cards)
    ]

    card_count = [1] * len(cards)

    for idx, winning_numbers, card_numbers in card_id_to_numbers:
        hits = wins_for_card(winning_numbers, card_numbers)

        for n in range(hits):
            card_count[idx + n + 1] += card_count[idx]

    return sum(card_count)


def test_part_1():
    return_value = check_file_p1('day4_tests.txt')
    if return_value != 13:
        print(f'[part1] expected 13 got {return_value}')
        sys.exit(1)


def test_part_2():
    return_value = check_file_p2('day4_tests.txt')
    if return_value != 30:
        print(f'[part2] expected 30 got {return_value}')
        sys.exit(1)


def part_1():
    print(f"[part1] {check_file_p1('day4.txt')}")


def part_2():
    print(f"[part2] {check_file_p2('day4.txt')}")


test_part_1()
test_part_2()
part_1()
part_2()
