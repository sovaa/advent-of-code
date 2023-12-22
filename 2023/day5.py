import sys
from pprint import pprint

steps = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location'
]


def src_to_dst(src, dst_map):
    """
    :param src (79, 14, 55, 13)
    :param dst_map [(50, 98, 2), (52, 50, 48)]

    :return [(79, 81), (14, 14), (55, 57), (13, 13)]
    """
    results = list()

    for source in src:
        found = False

        for dest_start, source_start, length in dst_map:
            # print(f'source: {source} dest_start: {dest_start} source_start: {source_start} length: {length}')
            # check if the source is in the range, then add the offset
            if source_start <= source < source_start + length:
                results.append(dest_start + (source - source_start))
                found = True
                break

        # if not in the ranges, the source is the same as the destination number
        if not found:
            results.append(source)

    return results


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    seeds, lines = lines[0], lines[2:]
    source = [int(s) for s in seeds.split(':')[1].split()]

    current_header = lines[0].split()[0]
    step_data = {
        current_header: list()
    }

    for line in lines[1:]:
        line = line.strip()
        if not len(line):
            continue

        if not line[0].isdigit():
            current_header = line.split()[0]
            step_data[current_header] = list()
            continue

        step_data[current_header].append([int(s) for s in line.split()])

    # iterate from seeds until we get to locations
    for step in steps:
        source = src_to_dst(source, step_data[step])

    return min(source)


def process_part_2(file_name):
    return 0


def test_part_1():
    """
    What is the lowest location number that corresponds to any of the initial seed numbers?

    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
    """

    seeds = (79, 14, 55, 13)
    seed_to_soil = [
        (50, 98, 2),
        (52, 50, 48)
    ]
    expected = [81, 14, 57, 13]

    predicted = src_to_dst(seeds, seed_to_soil)

    if predicted != expected:
        print(f'[part1] expected {expected} got {predicted}')
        sys.exit(1)

    return_value = process_part_1('day5_tests.txt')
    if return_value != 35:
        print(f'[part1] expected 35 got {return_value}')
        sys.exit(1)


def test_part_2():
    pass


def part_1():
    print(f"[part1] {process_part_1('day5.txt')}")


def part_2():
    print(f"[part2] {process_part_2('day5.txt')}")


test_part_1()
# test_part_2()
part_1()
# part_2()
