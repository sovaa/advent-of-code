import itertools


def process(file_name, dist=1):
    with open(file_name, 'r') as f:
        chart = [line.replace("\n", "") for line in f.readlines()]

    # dist means distance between galaxies, but we only add dist-1 empty rows/cols
    dist -= 1

    rows_to_expand = list()
    cols_to_expand = list()

    # find empty rows
    for row_nr, row in enumerate(chart):
        if all((c == '.' for c in row)):
            rows_to_expand.append(row_nr)

    # find empty columns
    for col_nr in range(len(chart[0])):
        all_empty = True
        for row_nr, row in enumerate(chart):
            if row[col_nr] != '.':
                all_empty = False
                break
        if all_empty:
            cols_to_expand.append(col_nr)

    # find galaxies
    galaxies = list()
    for row_nr, row in enumerate(chart):
        for col_nr, col in enumerate(row):
            if col == '#':
                galaxies.append((row_nr, col_nr))

    # expand columns first by adjusting its coordinates (in reverse order, so we don't mess up the indices)
    for col_nr in reversed(cols_to_expand):
        for galaxy_idx, (galaxy_row, galaxy_col) in enumerate(galaxies):
            if galaxy_col > col_nr:
                galaxies[galaxy_idx] = (galaxy_row, galaxy_col + dist)

    # then expand the rows, also in reverse order
    for row_nr in reversed(rows_to_expand):
        for galaxy_idx, (galaxy_row, galaxy_col) in enumerate(galaxies):
            if galaxy_row > row_nr:
                galaxies[galaxy_idx] = (galaxy_row + dist, galaxy_col)

    # manhattan distance between all pairs of galaxies
    all_distances = 0
    for galaxy_a, galaxy_b in itertools.combinations(galaxies, 2):
        all_distances += abs(galaxy_b[0] - galaxy_a[0]) + abs(galaxy_b[1] - galaxy_a[1])

    return all_distances


def test_part_1():
    assert process('day11_tests.txt', dist=2) == 374


def test_part_2():
    assert process('day11_tests.txt', dist=10) == 1030
    assert process('day11_tests.txt', dist=100) == 8410


def part_1():
    result = process('day11.txt', dist=2)
    assert result == 9543156
    print(f"[part1] {result}")


def part_2():
    result = process('day11.txt', dist=1_000_000)
    assert result == 625243292686
    print(f"[part2] {result}")


test_part_1()
test_part_2()
part_1()
part_2()
