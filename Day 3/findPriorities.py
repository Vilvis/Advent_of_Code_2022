# Open input file
f = open("rucksackes_contents.txt", "r");

# Input is long string with chunk separated by "\n" char so split
rucksackes = f.read().splitlines()

# Define a array containing the groups for the bagde search
elfs_groups = []
for x in range(int(len(rucksackes)/3)):
    elfs_groups.append(rucksackes[3*x:3*x+3])
    
# Define priorities and a function to return given a char input
alpha_list = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def priorities(item):
    return alpha_list.index(item)    

# Set a totatl priorities count
totalPriorities = 0;
totalBadgePriorities = 0;

# Loop through all rucksackes 
for rsack in rucksackes:
    # print("On rucksack number: ",rucksackes.index(rsack))
    
    # Find index of speration betweem compartmnets
    m = int(len(rsack)/2)
    
    # Separate the array
    firstComp = rsack[0:m]
    secondComp = rsack[m:2*m]
    # print(firstComp)
    # print(secondComp)
    
    # Find common char
    for i in firstComp:
        item_p = 0
        # if .find is positive then 2 compartments have common item
        # Calculate priorities, add it to total count then we can stop 
        # the iteration in this rucksacke and move on to the next one
        if(secondComp.find(i)>-1):
            item_p = priorities(i)
            # print("Common string: ",i)
            break
             
    # print("\n")
    if(item_p > 0):
            totalPriorities += item_p
    else:
        
        next

# Loop trough all groups
for group in elfs_groups:
    
    badge_p = 0
    # Find the common char5
    for i in group[0]:
        
        # min(group[1].find(i),0) returns -1 if not match and 0 if match
        # so if match in both then sum is 0, if 1 match then sum is negative
        if( min(group[1].find(i),0) + min(group[2].find(i),0) >= 0):
            # print("Hey this is a match: ",i)
            badge_p = priorities(i)
            break
            
    if(item_p > 0):
            totalBadgePriorities += badge_p
    else:
        next
    

print("\nThe total sum of priorities is: ",totalPriorities)
print("\nThe total sum of badges priorities is: ",totalBadgePriorities,"\n")
    
            
            
    
    
    
