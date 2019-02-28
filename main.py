#!/usr/bin/python3

import random
from itertools import permutations
from solver import findSolutions, combinations

LargeNumbers = [ 25, 50, 75, 100 ]
SmallNumbers = [ 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10 ]

# Append the number lists
availableCards = LargeNumbers +  SmallNumbers

# Calculate all of the combinations of 6 entries of the availableCards
orderedCombinations = list(combinations(availableCards, 6))

# Remove Duplicate Number Combinations
cardCombinations = list(set(orderedCombinations))
print("Number of Unique Combinations: " , len(cardCombinations))

# Write a function that generates a random number between 100 and 999 (simples)
def generateTarget():
    # Can modify this to be incremental later on if desired :)
    return random.randrange(100,999)
target = generateTarget()

target = 987

numberofSolutionsPerCombinationList = []
for cardCombo in cardCombinations:
    solutions = findSolutions(target, cardCombo)[0]
    if(solutions == []):
        numberofSolutionsPerCombinationList.append([cardCombo,0])
    else:
        print([cardCombo,len(solutions[0])])
        numberofSolutionsPerCombinationList.append([cardCombo,len(solutions[0])])

print(numberofSolutionsPerCombinationList)
