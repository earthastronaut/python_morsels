#!python


def stackpair(blocks):
    for i in range(0, len(blocks)):
        j = len(blocks) - i - 1
        if i == j:
            cube = blocks[i]
            yield i, i, cube, cube
        elif j > i:
            left = blocks[i]
            right = blocks[j]
            minlength = min(left, right)
            maxlength = max(left, right)
            yield i, j, minlength, maxlength
        else:
            break


def check_is_stackable_blocks(blocks):
    length = None
    for i, j, minlength, maxlength in stackpair(blocks):
        print(i, j, length, minlength, maxlength)
        if length is None:
            length = minlength
        elif length < maxlength:
            print("error")
            return False
    else:
        return True


def format_output(output):
    if output:
        print("Yes")
    else:
        print("No")


def check_is_stackable_stacks(stacks):
    return [
        "Yes" if is_stackable else "No"
        for is_stackable in map(check_is_stackable_blocks, stacks)
    ]


def parse_input_stdin():
    T = int(input())
    stacks = []
    for _ in range(T):
        _ = input()
        blocks = list(map(int, input().split()))
        stacks.append(blocks)
    return stacks


def parse_input_file(fp):
    with open(fp) as buffer:
        lines = buffer.read().splitlines()
    T = int(lines[0])
    stacks = []
    for line in lines[2::2]:
        blocks = list(map(int, line.split()))
        stacks.append(blocks)
    return stacks


################################################

if __name__ == "__main__":
    input_fp = "input3.txt"
    output_fp = "output3.txt"
    stacks = parse_input_file(input_fp)
    actual = check_is_stackable_stacks([stacks[1]])
    # with open(output_fp) as buffer:
    #     expected = buffer.read().splitlines()
    # for a, e in zip(actual, expected):
    #     if a != e:
    #         raise ValueError(f"{actual} != {expected}")
