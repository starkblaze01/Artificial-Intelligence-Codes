import random
global_hillClimbing = 1
global_beamSearch = 1
global_variableNeighbourhoodDescent = 1


def clauseGen(n, m, k):
    var = []
    clauses = []
    doneVars = []

    # Generate vars
    for i in range(n):
        char = chr(random.randint(97, 122))
        while char in var:
            char = chr(random.randint(97, 122))
        var.append(char)
    print("Variables are: ")
    print(var)

    for i in range(m):
        clause = []
        for j in range(k):
            a = random.choice(var)
            while a in clause or a in doneVars:
                a = random.choice(var)
            clause.append(a)
            doneVars.append(a)
            if len(doneVars) == len(var):
                doneVars = []

        for x in clauses:
            if(set(x) == set(clause)):
                if clause in clauses:
                    clauses.remove(clause)
                    j -= 1

        clauses.append(clause)
    # print(clauses)
    finalclause = []

    for i in range(len(clauses)):
        for j in range(len(clauses[i])):
            finalclause.append(clauses[i][j])
    # print(finalclause)
    superfinalclause = ""
    i = 0
    while i < len(finalclause):
        superfinalclause = superfinalclause + "("
        for j in range(k):
            superfinalclause = superfinalclause + finalclause[i] + "|"
            i += 1
        superfinalclause = superfinalclause[:-1]
        superfinalclause = superfinalclause + ")&"
    superfinalclause = superfinalclause[:-1]
    print("Expression Generated is: "+superfinalclause)
    return superfinalclause, var


def main():
    n = int(input('Enter the number of variables: '))
    m = int(input('Enter the number of clauses: '))
    k = int(input('Enter the number vars in one clause: '))
    x = clauseGen(n, m, k)
    # print(x[0])
    # stm = [0, 0, 0, 0, 1]
    a = []
    for i in range(n):
        a.append(str(random.randint(0, 1)))
    # print(x, a)
    # parse(x, a)
    print(a)
    neighbour = 3
    width = int(input("Enter the beam width: "))
    hillClimbing(x, a, m, n)
    beamSearch(width, x, a, m, n)
    variableNeighbourhoodDescent(neighbour, x, a, m, n)
    print("No. of states explored in Hill Climbing: ", global_hillClimbing)
    print("No. of states explored in Beam Search: ", global_beamSearch)
    print("No. of states explored in Variable Neighbourhood Descent: ",
          global_variableNeighbourhoodDescent)


def parse(x, stm):
    # print(x[0], x[1], stm)
    y = x[0]
    for i in range(len(x[1])):
        y = y.replace(x[1][i], stm[i])
        # print(x[1][i], stm[i])
    # print(y)
    yy = y.split("&")
    # print(yy)
    count_true = 0
    count_false = 0
    for i in range(len(yy)):
        if eval(yy[i]) == 1:
            count_true += 1
        else:
            count_false += 1

    # print(count_true, count_false)
    # print("lol")
    return count_true


def hillClimbing(x, a, m, n):
    frontier = []
    max_heuristicValueIndex = 0
    heuristic_values = []
    for i in range(n):
        new_a = []
        for j in range(len(a)):
            new_a.append(a[j])
        if a[i] == "0":
            new_a[i] = "1"
            frontier.append(new_a)
        else:
            new_a[i] = "0"
            frontier.append(new_a)
        print(new_a)
        heuristic_count = parse(x, frontier[i])
        heuristic_values.append(heuristic_count)
        if heuristic_count == m:
            return frontier[i]
    global global_hillClimbing
    global_hillClimbing += 1
    max_heuristicValueIndex = heuristic_values.index(max(heuristic_values))
    print(heuristic_values[max_heuristicValueIndex])
    hillClimbing(x, frontier[max_heuristicValueIndex], m, n)


def beamSearch(width, x, a, m, n):
    frontier = []
    # max_heuristicValueIndex = 0
    heuristic_values = []
    for i in range(n):
        new_a = []
        for j in range(n):
            new_a.append(a[j])
        if a[i] == "0":
            new_a[i] = "1"
            frontier.append(new_a)
        else:
            new_a[i] = "0"
            frontier.append(new_a)
        # print(new_a)
        heuristic_count = parse(x, frontier[i])
        heuristic_values.append(heuristic_count)
        if heuristic_count == m:
            return frontier[i]
    global global_beamSearch
    global_beamSearch += width
    beam = []
    for pp in range(len(heuristic_values)):
        beam.append(heuristic_values[pp])
    beam.sort(reverse=True)
    print(beam)
    getMax = []
    for l in range(width):
        print(beam[l])
        getMax.append(beam[l])
    maxFrontiers = []
    # print(frontier)
    for ll in range(width):
        print(frontier[heuristic_values.index(getMax[ll])])
        maxFrontiers.append(frontier[heuristic_values.index(getMax[ll])])
    # max_heuristicValueIndex = heuristic_values.index(max(heuristic_values))
    # print(heuristic_values[max_heuristicValueIndex])
    for i in maxFrontiers:
        check = beamSearch(width, x, i, m, n)
        if(parse(x, check) == m):
            break
    return maxFrontiers[0]


def variableNeighbourhoodDescent(neighbour, x, a, m, n):
    frontier = []
    # max_heuristicValueIndex = 0
    heuristic_values = []
    for i in range(n):
        new_a = []
        for j in range(n):
            new_a.append(a[j])
        if a[i] == "0":
            new_a[i] = "1"
            frontier.append(new_a)
        else:
            new_a[i] = "0"
            frontier.append(new_a)
        # print(new_a)
        heuristic_count = parse(x, frontier[i])
        heuristic_values.append(heuristic_count)
        if heuristic_count == m:
            return frontier[i]
    global global_variableNeighbourhoodDescent
    global_variableNeighbourhoodDescent += 3
    beam = []
    for pp in range(len(heuristic_values)):
        beam.append(heuristic_values[pp])
    beam.sort()
    # print(beam)
    getImproveChild = []
    it = 0
    flag = True
    while flag:
        for lp in range(len(beam)):
            if beam[lp] > parse(x, a):
                getImproveChild.append(beam[lp])
                print(getImproveChild)
                it += 1
            if it == 3:
                flag = False
                break
        getImproveChild.sort(reverse=True)
    # for l in range(neighbour):
    #     print(beam[l])
    #     getImproveChild.append(beam[l])

    theNeighbours = []
    # print(getImproveChild)
    for ll in range(neighbour):
        print(frontier[heuristic_values.index(getImproveChild[ll])])
        theNeighbours.append(
            frontier[heuristic_values.index(getImproveChild[ll])])
    # max_heuristicValueIndex = heuristic_values.index(max(heuristic_values))
    # print(heuristic_values[max_heuristicValueIndex])
    for i in range(neighbour):
        check = variableNeighbourhoodDescent(
            neighbour, x, theNeighbours[i], m, n)
        if(parse(x, check) == m):
            return theNeighbours[i]
    return theNeighbours[0]


if __name__ == "__main__":
    main()
