from itertools import product


def maximize_expression(K, M, lists):
    options = []
    for i in product(*lists):
        options.append(sum([x**2 for x in i]) % M)
    return max(options)



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
