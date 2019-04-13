import itertools
import random


def cal_energy(x, y, distance):
    minm = float("inf")
    flag = 1
    new_x = []
    l = y
    energy = 0
    while(flag):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if k == 3:
                        index = -1
                    else:
                        index = k
                    energy = energy + 0.5 * \
                        (distance[i][j])*(x[l][i][k])*(x[l][j][index+1])
        print(" Energy for: ", x[l], " is: ", energy)
        if energy <= minm:
            minm = energy
            new_x = x[l]
        if l < len(x)-1:
            l += 1
        else:
            l = 0
        if l == y:
            flag = 0
        energy = 0
    return new_x


def main():
    comb = ([[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]])
    x = list(itertools.permutations(comb))
    y = random.randint(0, len(x))
    # print(x)
    # points located at (0,0),(0,1),(1,1),(1,0)
    ##  D(1,0) ------- C(1,1)
    #   |                 |
    #   |                 |
    #   |                 |
    ##  A(0,0) ------- B(0,1)
    distance = ([[0, 1, (2)**0.5, 1], [1, 0, 1, (2)**0.5],
                 [(2)**0.5, 1, 0, 1], [1, 1, (2)**0.5, 0]])
    # print("Distance Matrix is: ", distance)
    print("Points are: (0,0),(0,1),(1,0),(1,1)")
    new_x = cal_energy(x, y, distance)
    print("Path to be follwed:", new_x)


if __name__ == "__main__":
    main()
