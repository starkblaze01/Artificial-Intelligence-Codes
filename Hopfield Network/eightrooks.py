import itertools
import random


def calc_energy(pos):
    e1 = 0
    e2 = 0
    accumulator = 0
    for i in range(len(pos)):
        for j in range(len(pos)):
            accumulator += pos[i][j]
        e1 += (accumulator-1)**2
        accumulator = 0

    for i in range(len(pos)):
        for j in range(len(pos)):
            accumulator += pos[j][i]
        e2 += (accumulator-1)**2
        accumulator = 0
    print(e1, e2)
    return e1 + e2


def main():
    states = [[1, 0, 0, 0, 0, 0, 0, 0], [
        0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    perm = list(itertools.permutations(states))
    rep = list(itertools.product(states, repeat=8))

    random.shuffle(perm)

    index = random.randint(0, len(perm)-1)

    while(calc_energy(perm[index]) != 0):
        index += 1
        if index == len(perm) - 1:
            index = 0

    print('Solution is', perm[index])


if __name__ == "__main__":
    main()
