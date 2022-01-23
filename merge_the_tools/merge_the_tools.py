#!python


def run_merge_the_tools(string, k):
    n = len(string)
    bins = list(range(0, n + k, k))
    parts = []
    for i, j in zip(bins[:-1], bins[1:]):
        substring = string[i:j]
        unique = "".join({k:0 for k in substring}.keys())
        parts.append(unique)

    formatted = "\n".join(parts)
    return formatted


def merge_the_tools(string, k):
    output = run_merge_the_tools(string, k)
    print(output)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
