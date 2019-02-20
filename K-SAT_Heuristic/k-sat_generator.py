import random


def main():
    n = int(input('Enter the number of variables: '))
    m = int(input('Enter the number of clauses: '))
    k = int(input('Enter the number vars in one clause: '))

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


if __name__ == "__main__":
    main()
