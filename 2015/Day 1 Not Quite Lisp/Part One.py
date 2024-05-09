# Define the path to your file here; ensure it's either a full path or correct relative path
filepath = "path/to/your/filename.txt" 

# Initialize the counter for tracking the floor count
floor_count = 0

# Open the file 
with open(filepath, "r") as file:
    instructions = file.read()  # Read the entire file into a single string

    # Loop through each character in the string
    for char in instructions:
        if char == "(":
            floor_count += 1  # Increment for every '('
        elif char == ")":
            floor_count -= 1  # Decrement for every ')'

# Output the final floor count
print("Final floor count:", floor_count)