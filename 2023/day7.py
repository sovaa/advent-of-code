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


"""
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
    FIVE_OF_A_KIND = 10
"""


class Offset:
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    # STRAIGHT = 4
    # FLUSH = 5
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    # STRAIGHT_FLUSH = 8
    # ROYAL_FLUSH = 9
    FIVE_OF_A_KIND = 6


def leftmost_high_card(hand):
    part_scores = [h * 14**(5 - i) for i, h in enumerate(hand)]
    # print(f"[parts] {part_scores} = {sum(part_scores)}")
    return sum(part_scores)


MAX_HIGH_CARD_SCORE = leftmost_high_card([max(card_to_int.values())] * 5)  # 1555540
MIN_HIGH_CARD_SCORE = leftmost_high_card([min(card_to_int.values())] * 5)  # 222220
MIN_HIGH_CARD_OFFSET = 2 * 10**6 - MIN_HIGH_CARD_SCORE                     # 1777780


def score(hand, kind, offset, remainder):
    # if both have the same four of a kind, the remainder would decide the winner
    # return four_cards_of * 10**Offset.FOUR_OF_A_KIND + remainder
    # return kind * 10**offset + remainder

    # part one we check each card from left one by one unsorted to compare high card, not the total hands' high card
    leftmost = leftmost_high_card(hand)
    # the_score = (kind * 14**(offset+7)) + leftmost
    the_score = (1 * 14**(offset+7)) + leftmost  # all cards are equal in part 1
    # print(f'[score {hand}] \t (kind * 14**offset) + leftmost_high_card(hand):')
    # print(f"[score {hand}] \t ({kind} * 14**{offset+7}) + {leftmost} = {the_score}")
    # print()
    return the_score


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


def five_of_a_kind(counter):
    for card, count in counter.items():
        if count == 5:
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

    # no royal flush in p1
    # if royal_flush(hand):
    #     return score(hand, 1, Offset.ROYAL_FLUSH, 0)

    # no colors
    # elif straight_flush(hand, counter):
    #     return high_card(hand) * 10**Offset.STRAIGHT_FLUSH

    if five_of_a_kind(counter):
        five_cards_of = [card for card, count in counter.items() if count == 5][0]

        return score(hand, five_cards_of, Offset.FIVE_OF_A_KIND, 0)

    elif four_of_a_kind(counter):
        remainder = [card for card, count in counter.items() if count == 1][0]
        four_cards_of = [card for card, count in counter.items() if count == 4][0]

        return score(hand, four_cards_of, Offset.FOUR_OF_A_KIND, remainder)

    elif full_house(counter):
        threes = [card for card, count in counter.items() if count == 3][0]
        twos = [card for card, count in counter.items() if count == 2][0]

        return score(hand, threes, Offset.FULL_HOUSE, twos)

    # no colors
    # elif flush(hand, counter):
    #     return high_card(hand) * 10**Offset.FLUSH

    # elif straight(counter):
    #     return score(hand, high_card(hand), Offset.STRAIGHT, 0)

    elif three_of_a_kind(counter):
        threes = [card for card, count in counter.items() if count == 3][0]
        return score(hand, threes, Offset.THREE_OF_A_KIND, 0)

    elif two_pair(counter):
        the_pairs = [card for card, count in counter.items() if count == 2]
        return score(hand, max(the_pairs), Offset.TWO_PAIR, min(the_pairs))

    elif pair(counter):
        the_pair = [card for card, count in counter.items() if count == 2][0]
        return score(hand, the_pair, Offset.PAIR, 0)

    return score(hand, high_card(hand), Offset.HIGH_CARD, 0)


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
    return score_hands(hands, lines)


def score_hands(hands, lines):
    sorted_hands = sorted(hands, key=lambda x: x[1], reverse=False)

    # print(lines)
    # print(hands)
    # print(sorted_hands)

    total_winnings = 0
    for rank, hand in enumerate(sorted_hands):
        bid = hand[2]
        result = bid * (rank + 1)
        # print(f"[result] {bid} * ({rank} + 1) = {result}")
        total_winnings += result

    """
    for hand in sorted_hands[:20]:
        print(f'{hand[0]}\t{hand[1]}\t{hand[2]}\t{lines[hand[0]]}')

    print()
    print()

    for hand in reversed(sorted_hands[-20:]):
        print(f'{hand[0]}\t{hand[1]}\t{hand[2]}\t{lines[hand[0]]}')
    """

    return total_winnings


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    return 0


def test_part_1():
    assert hand_to_int("33332") > hand_to_int("2AAAA")
    assert hand_to_int("77888") > hand_to_int("77788")

    return_value = process_part_1('day7_tests.txt')
    if return_value != 6440:
        print(f'[test part1] expected 6440 got {return_value}')
        sys.exit(1)
    else:
        print(f'[test part1] {return_value}')


def test_part_2():
    pass


def part_1():
    p1_answer = process_part_1('day7.txt')
    print(f"[part1] {p1_answer}")

    assert p1_answer == 251121738


def part_2():
    pass


test_part_1()
test_part_2()
part_1()
part_2()
