#!/usr/bin/python3

import random
from solver import findSolutions

LargeNumbers = [ 25, 50, 75, 100 ]
SmallNumbers = [ 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10 ]

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

# Append the number lists
availableCards = LargeNumbers +  SmallNumbers

# Calculate all of the combinations of 6 entries of the availableCards
orderedCombinations = list(combinations(availableCards, 6))

# Remove Duplicate Number Combinations
cardCombinations = set(orderedCombinations)
print("Number of Unique Combinations: " , len(cardCombinations))

# Write a function that generates a random number between 100 and 999 (simples)
def generateTarget():
    # Can modify this to be incremental later on if desired :)
    return random.randrange(100,999)
target = generateTarget()


# This function runs through all of the card combinations it is passed and returns the number of them that can solve for the specified target value
def bruteForce(target, availableCombinations):
    validsolutions = []
    for combination in availableCombinations:
        validsolutions.extend(findSolutions(target, combination))
    return validsolutions

solutions = bruteForce(target, cardCombinations)

print(solutions)
