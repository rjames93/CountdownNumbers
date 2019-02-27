#!/usr/bin/python3

import random
from solver import findSolutions, combinations

LargeNumbers = [ 25, 50, 75, 100 ]
SmallNumbers = [ 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10 ]

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

target = 100
# This function runs through all of the card combinations it is passed and returns the number of them that can solve for the specified target value
def bruteForce(target, availableCombinations):
    validsolutions = []
    for combination in availableCombinations:
        validsolutions.extend(findSolutions(target, combination))
    return validsolutions

solutions = bruteForce(target, cardCombinations)

print(solutions)
