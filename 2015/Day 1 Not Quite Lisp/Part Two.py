# Define the path to your file here; ensure it's either a full path or correct relative path
filepath = "path/to/your/filename.txt"

# Initialize counters: 
# 'floor_count' tracks the current floor level.
# 'counter' tracks the position of the character being processed.
floor_count = 0
counter = 0

# Open and read the file using a 'with' statement to ensure proper handling of file resources.
with open(filepath, "r") as file:
    instructions = file.read()  # Read the entire file content into a single string.

    # Loop through each character in the string to determine the floor changes.
    for char in instructions:
        counter += 1  # Increment the character position counter.
        if char == "(":
            floor_count += 1  # Increment the floor count for '('.
        elif char == ")":
            floor_count -= 1  # Decrement the floor count for ')'.
            # Check if Santa has entered the basement (floor level below 0).
            if floor_count < 0:
                break  # Exit the loop once the basement is entered.

# Output the character position at which the basement is entered.
print("Basement entered on character: " + str(counter))