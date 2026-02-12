# Sherlock Holmes must determine the prime suspect in a case based on collected clues.
# Each suspect has a number of clues pointing toward them.
# The program analyzes the clues and identifies the most likely suspect.

suspects = [
    {"name": "Mr. Green", "clues": 3},
    {"name": "Ms. Scarlet", "clues": 5},
    {"name": "Colonel Mustard", "clues": 2}
]

# how it works 
# Accept suspect details from the user

# Store suspect data in a list

# Compare clue counts for each suspect

# Identify the suspect with the highest number of clues

# Display the prime suspect

# Step by step 

# Start

# Read number of suspects

# For each suspect:

# Read name and clue count

# Store in a list

# Set first suspect as prime suspect

# Compare clues of each suspect

# If a suspect has more clues, update prime suspect

# Display prime suspect

# End


suspects = [{"name": "Mr. Green", "clues": 3},
    {"name": "Ms. Scarlet", "clues": 5},
    {"name": "Colonel Mustard", "clues": 2}]

n = int(input("Enter number of suspects: 3 "))

for i in range(n):
    name = input("Enter suspect name: Ms. Scarlet ")
    clues = int(input("Enter number of clues found: 5 "))

    suspects.append({ "name": "Mr. Green", "clues": 3})
suspects.append({"name": "Ms. Scarlet", "clues": 5})
suspects.append({"name": "Colonel Mustard", "clues": 2
    })

prime_suspect = suspects[0]

for suspect in suspects:
    if suspect["clues"] > prime_suspect["clues"]:
        prime_suspect = suspect

print("Sherlock Holmes' Conclusion:")
print(f"Prime suspect is {prime_suspect['Ms. Scarlet']} with {prime_suspect['5']} clues.")
