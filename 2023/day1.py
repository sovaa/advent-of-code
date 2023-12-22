import sys

numbers = list()

name_to_num = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def line_has_name(_line):
    for k in name_to_num.keys():
        if k in _line:
            return True
    return False


def check_line(line):
    digits = list()
    line = line.replace('\n', '')
    found_end = False
    found_start = False

    new_line_start = None
    new_line_end = None

    while line_has_name(line):
        for i in range(len(line)):
            for k, v in name_to_num.items():

                if not found_start:
                    if line[i:].startswith(k):
                        found_start = True
                        new_line_start = line.replace(k, v, 1)

                if not found_end:
                    if i == 0 and line.endswith(k):
                        found_end = True
                        new_line_end = v.join(line.rsplit(k, 1))
                    elif line[:-i].endswith(k):
                        found_end = True
                        new_line_end = v.join(line.rsplit(k, 1))

                if found_start and found_end:
                    break
            if found_start and found_end:
                break
        if found_start and found_end:
            break

    if new_line_start is None:
        new_line_start = line
    if new_line_end is None:
        new_line_end = line

    for c in new_line_start:
        if c.isdigit():
            digits.append(c)
            break

    for c in reversed(new_line_end):
        if c.isdigit():
            digits.append(c)
            break

    assert len(digits) == 2
    return int(''.join(digits))


def test():
    with open('day1_tests.txt', 'r') as f:
        for line_and_answer in f.readlines():
            line_and_answer = line_and_answer.replace('\n', '')

            __line, answer = line_and_answer.split(',')
            answer = int(answer)
            retval = check_line(__line)

            if retval != answer:
                print(f"failed on line: {__line}")
                print(f"expected: {answer}, got: {retval}")
                assert False


test()

if len(sys.argv) > 1:
    _line = sys.argv[1]
    print(check_line(_line))
else:
    numbers = list()
    total = 0

    with open('day1.txt', 'r') as f:
        for _line in f.readlines():
            number = check_line(_line)
            if number:
                numbers.append(number)

    print(sum(numbers))
