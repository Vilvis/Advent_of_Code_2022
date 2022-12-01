##
## Day 1 - Advent of Code 2022
##

# Open input file
f = open("elvesCaloriesList.txt", "r");

# Input is long string with chunk separated by 2 x "\n" char so split
elves = f.read().rsplit("\n\n")

# For each chunk the individuall food count is relevant

# Set up a record of each elf load
elvesCal = []

# Iter trough and find what each elf is carrying
for elf in elves:
    
    # split int with "\n" again
    foodCals = elf.rsplit("\n");
    
    # Loop trough and add each nug of food to the elf's load
    totalCal = 0;
    for nug in foodCals:
        totalCal += int(nug) 
    
    # Append new sum
    elvesCal.append(totalCal)
    
# Sort the list to Decreasing
elvesCal.sort(reverse = True)

# Print the results
printTemplate = """
The elf carrying the most food is carrying: {:,} Calories

The top 3 elfs carrying the most food are:

1st {:,} Calories
2nd {:,} Calories   For a total of: {:,} Calories
3rd {:,} Calories
"""

print(printTemplate.format(elvesCal[0],elvesCal[0],elvesCal[1],sum(elvesCal[0:3]),elvesCal[2]))