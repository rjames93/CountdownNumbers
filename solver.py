# Ahahahaha stack overflow I love you soo much.
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


# This function takes a target number and 6 card numbers and finds all the solutions
def findSolutions(target, numberCards):
    solutions = []

    solutions = bruteForceSolve(target, numberCards)

    return solutions

def recurseSolve(target, numberCards, solutionChain):
    if(target in numberCards):
        solutionChain += "; = " + str(target)
        print(solutionChain)
        return solutionChain
    elif( all (x > 0 for x in numberCards)):
        for pair in list(combinations(numberCards, 2)):
            # Make a local copy for the recursion
                nextCards = numberCards[:]
                # Remove the two cards chosen to be combined in someway
                nextCards.remove(pair[0])
                nextCards.remove(pair[1])

                # Perform the Addition operation (which is independent on order for the result)
                newSolutionChain = solutionChain + ";" + str(numberCards) + "->" + "(" + str(pair[0]) + "+" + str(pair[1]) + ")"
                recurseSolve(target, nextCards + [pair[0]+pair[1]], newSolutionChain)

                # Perform the Multiplicative Operation which is also independent
                newSolutionChain = solutionChain + ";" + str(numberCards) + "->" + "(" + str(pair[0]) + "*" + str(pair[1]) + ")"
                recurseSolve(target, nextCards + [pair[0]*pair[1]], newSolutionChain)

                # Check divisions don't create floats and do both orders
                if( isinstance((pair[0] / pair[1]), float) == False ):
                    newSolutionChain = solutionChain + ";" + str(numberCards) + "->" + "(" + str(pair[0]) + "/" + str(pair[1]) + ")"
                    recurseSolve(target, nextCards + [pair[0]/pair[1]], newSolutionChain)

                if( isinstance((pair[1] / pair[0]), float) == False ):
                    newSolutionChain = solutionChain + ";" + str(numberCards) + "->" + "(" + str(pair[1]) + "/" + str(pair[0]) + ")"
                    recurseSolve(target, nextCards + [pair[1]/pair[0]], newSolutionChain)

                # Now do subtraction both orders after checking that the result is non negative
                if( (pair[0] - pair[1] > 0) ):
                    newSolutionChain = solutionChain + ";" + str(numberCards) + "->" + "(" + str(pair[0]) + "-" + str(pair[1]) + ")"
                    recurseSolve(target, nextCards + [pair[0]-pair[1]], newSolutionChain)

                if( (pair[1] - pair[0] > 0) ):
                    newSolutionChain = solutionChain + ";" + str(numberCards) + "->" + "(" + str(pair[1]) + "-" + str(pair[0]) + ")"
                    recurseSolve(target, nextCards + [pair[1]-pair[0]], newSolutionChain)



    return

def bruteForceSolve(target, numberCards):
    cardsavailable = list(numberCards)

    recurseSolve(target, cardsavailable, "")


    return solutions


