# Open and split input string into array of rounds in the form: "[["A X"],["C Y"],...""
# Each row is a round
f = open("input.txt", "r");
rounds = f.read().rsplit("\n")


# Define the outcome of Rock Paper Scissor 
# (Row -> Elf choice )
# (Col -> Our choice )
#
#            R   P   S
scores = [[  0,  1, -1],  # Rock
          [ -1,  0,  1],  # Paper
          [  1, -1,  0]]  # Scissors

# Points earn based on outcome of the rounds
outcome_points={
       -1: 0 ,
       0: 3,
       1: 6
}

# Part 2 - Outcome to force based on input stategy
# X -> Loss -1
# Y -> Draw 0
# Z -> Loss 1
fates={
        'X': -1,
        'Y': 0,
        'Z': 1
    }

# This function returns an index based on the move for the scores matrix  
def indexMove(letter):
    switch={
       'A': 0,
       'B': 1,
       'C': 2,
       'X': 0,
       'Y': 1,
       'Z': 2,
       }
    return switch.get(letter,"Invalid move")


# Set up score tracker for part 1 and part 2 
total_score_1 = 0;
total_score_2 = 0;

# Iterate through all the rounds
for x in rounds:
    
    # Initliaze score for the round 
    round_score = 0
    
    # Index the choices
    elf_choice = indexMove(x[0])
    tactic_choice = indexMove(x[2])
    
    # Find the outcome if Part 1 strategy
    results = scores[elf_choice][tactic_choice]
    
    # Find the outcome if Part 2 strategy
    # Start by finding the outcome of the round by reading strategy
    fate        = fates.get(x[2],"Invalid move")
    # Find the move played 
    fate_choice = scores[elf_choice].index(fate)
  
    # Calculate points and add to tracker
    total_score_1 += outcome_points.get(results,"Invalid result") + tactic_choice + 1;
    total_score_2 += outcome_points.get(fate,"Invalid result") + fate_choice + 1

# Print out 
print("The total score following strategy 1 is:", total_score_1)
print("The total score following strategy 2 is:", total_score_2)
    
    
