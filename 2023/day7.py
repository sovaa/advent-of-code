import sys
from collections import Counter

card_to_int = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Offset:
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


def royal_flush(hand):
    return sorted(hand) == [10, 11, 12, 13, 14]


def straight(hand):
    sorted_hand = sorted(hand)
    for i in range(1, len(sorted_hand)):
        if sorted_hand[i] - sorted_hand[i - 1] != 1:
            return False
    return True


def high_card(hand):
    return max(hand)


def three_of_a_kind(counter):
    for card, count in counter.items():
        if count == 3:
            return True
    return False


def four_of_a_kind(counter):
    for card, count in counter.items():
        if count == 4:
            return True
    return False


def full_house(counter):
    return three_of_a_kind(counter) and pair(counter)


def two_pair(counter):
    pairs = 0
    for card, count in counter.items():
        if count == 2:
            pairs += 1
    return pairs == 2


def pair(counter):
    for card, count in counter.items():
        if count == 2:
            return True
    return False


def hand_to_int(hand):
    hand = [card_to_int[card] for card in hand]
    counter = Counter(hand)

    if royal_flush(hand):
        return 1 * 10**Offset.ROYAL_FLUSH

    # no colors
    # elif straight_flush(hand, counter):
    #     return high_card(hand) * 10**Offset.STRAIGHT_FLUSH

    elif four_of_a_kind(counter):
        remainder = [card for card, count in counter.items() if count == 1][0]
        four_cards_of = [card for card, count in counter.items() if count == 4][0]

        # if both have the same four of a kind, the remainder would decide the winner
        return four_cards_of * 10**Offset.FOUR_OF_A_KIND + remainder

    elif full_house(counter):
        threes = [card for card, count in counter.items() if count == 3][0]
        twos = [card for card, count in counter.items() if count == 2][0]

        return threes * 10**Offset.FULL_HOUSE + twos

    # no colors
    # elif flush(hand, counter):
    #     return high_card(hand) * 10**Offset.FLUSH

    elif straight(counter):
        return high_card(hand) * 10**Offset.STRAIGHT

    elif three_of_a_kind(counter):
        threes = [card for card, count in counter.items() if count == 3][0]
        return threes * 10**Offset.THREE_OF_A_KIND

    elif two_pair(counter):
        the_pairs = [card for card, count in counter.items() if count == 2]
        return max(the_pairs) * 10**Offset.TWO_PAIR + min(the_pairs)

    elif pair(counter):
        the_pair = [card for card, count in counter.items() if count == 2][0]
        return the_pair * 10**Offset.PAIR

    return high_card(hand) * 10**Offset.HIGH_CARD


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

    hands = [[line[0], hand_to_int(line[1]), line[2]] for line in lines]
    sorted_hands = sorted(hands, key=lambda x: x[1], reverse=False)

    # print(lines)
    # print(hands)
    # print(sorted_hands)

    total_winnings = 0
    for rank, hand in enumerate(sorted_hands):
        bid = hand[2]
        total_winnings += bid * (rank + 1)

    for hand in sorted_hands[:50]:
        print(f'{hand[0]}\t{hand[1]}\t{hand[2]}\t{lines[hand[0]]}')
    return total_winnings


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
    print(f"[part1] {process_part_1('day7.txt')}")


def part_2():
    pass


test_part_1()
test_part_2()
part_1()
part_2()
