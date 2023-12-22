import sys

DEBUG = len(sys.argv) > 1

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
            # check if the source is in the range, then add the offset
            if source_start <= source < source_start + length:
                results.append(dest_start + (source - source_start))
                found = True
                break

        # if not in the ranges, the source is the same as the destination number
        if not found:
            results.append(source)

    return results


def src_range_to_dst(src, dst_map):
    """

    79+14-1 = 92
    79 to 92

    98+2-1 = 99
    98 to 99 -> out of range

    50+48-1 = 97
    50 to 97 -> in range
    intersection: (79, 92)
    dst range: (79+(50-98), 92+(50-98)) = (31, 44)

    -----

    55+13-1 = 67
    55 to 67

    98+2-1 = 99
    98 to 99 -> out of range

    50+48-1 = 97
    50 to 97 -> in range
    intersection: (55, 67)
    dst range: (55+(52-50), 67+(52-50)) = (57, 69)

    :param src [(79, 14), (55, 13)]
    :param dst_map [(50, 98, 2), (52, 50, 48)]

    :return [(81, 94), (57, 69)]
    """
    results = list()
    print(f"len(src): {len(src)}")

    for source_range in src:
        found = False

        for dest_start, source_start, length in dst_map:
            range_intersection = (
                max(source_range[0], source_start),
                min(source_range[0] + source_range[1] - 1, source_start + length - 1)
            )
            if DEBUG: print(f"\nrange intersection: {range_intersection} for destination {dest_start} {source_start} {length}")

            # we have at least some overlap, add the before and after (if any) plus the intersection
            if range_intersection[0] <= range_intersection[1]:
                found = True

                dest_range = [
                    range_intersection[0] + (dest_start - source_start),
                    range_intersection[1] - range_intersection[0] + 1  # plus one because range is inclusive
                ]

                # source:       [.......................]
                # dest:                 [..........]
                # prefix:       [......]
                # suffix:                           [...]
                # intersection:         [..........]

                # source:                  [............]
                # dest:                 [..........]
                # prefix:              |
                # suffix:                           [...]
                # intersection:            [.......]

                # source:           [.....]
                # dest:         [............]
                # prefix:      |
                # suffix:                     |
                # intersection:     [.....]

                src_start = source_range[0]
                src_end = source_range[0] + source_range[1] - 1
                prefix_start = source_range[0]
                prefix_end = range_intersection[0]
                suffix_start = range_intersection[1] + 1
                suffix_end = suffix_start + (src_end - range_intersection[1])

                if DEBUG: print('adding intersection:', dest_range)
                if DEBUG: print(f"source_range: {source_range}, range_intersection: {range_intersection}")
                if DEBUG: print(f"src_start: {src_start} src_end: {src_end}")
                if DEBUG: print(f"prefix_start: {prefix_start} prefix_end: {prefix_end}")
                if DEBUG: print(f"suffix_start: {suffix_start} suffix_end: {suffix_end}")

                results.append(dest_range)

                # add the prefix range part of the source range not in the intersection
                # if source_range[0] < range_intersection[0]:
                if prefix_start < prefix_end:
                    if DEBUG: print(f'adding prefix ({prefix_start}, {prefix_end})')
                    results.append([prefix_start, prefix_end])

                # add the suffix range part of the source range not in the intersection
                if suffix_end > suffix_end:
                    if DEBUG: print(f'source_range[0] + source_range[1]: {source_range[0] + source_range[1]} > range_intersection[1]: {range_intersection[1]}')
                    if DEBUG: print(f'adding suffix ({suffix_start}, {suffix_end})')
                    results.append([suffix_start, suffix_end])

            if DEBUG: print()

        if not found:
            # otherwise the destination is the same as the source
            if DEBUG: print('adding out-of-range:', source_range)
            results.append(source_range)

    return results


def get_min_location_for_seeds(source, lines):
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


def get_min_location_for_seed_ranges(source_ranges, lines):
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
        if DEBUG: print(f'step: {step} source: {sorted(source_ranges)}')
        if DEBUG: print(f'step data: {step_data[step]}')
        source_ranges = src_range_to_dst(source_ranges, step_data[step])
        if DEBUG: print(f'dest: {sorted(source_ranges)}')
        if DEBUG: print()

    return min([source for source, length in source_ranges if source > 0])


def process_part_1(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    seeds, lines = lines[0], lines[2:]
    source = [int(s) for s in seeds.split(':')[1].split()]

    return get_min_location_for_seeds(source, lines)


def process_part_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    seeds, lines = lines[0], lines[2:]
    source_ranges = [int(s) for s in seeds.split(':')[1].split()]

    source = list()
    for seed_start, seed_range in zip(source_ranges[::2], source_ranges[1::2]):
        source.append([seed_start, seed_range])

    return get_min_location_for_seed_ranges(source, lines)


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
    return_value = process_part_2('day5_tests.txt')
    print(f"[test_part_2] {return_value}")
    if return_value != 46:
        print(f'[part1] expected 46 got {return_value}')
        sys.exit(1)


def part_1():
    print(f"[part1] {process_part_1('day5.txt')}")


def part_2():
    print(f"[part2] {process_part_2('day5.txt')}")


#test_part_1()
test_part_2()
#part_1()
part_2()
