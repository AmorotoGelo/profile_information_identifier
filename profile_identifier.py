# Open txt file to read informations
with open(".\\user_information.txt", "r") as profile_identifier:
    # Ask user for a full name
    while True:
        name = input('Input a full name to identify information: ').strip()
# Read the informations in txt file
        user_information = profile_identifier.readlines()
# Use for loop to identify the name in txt file
        for line in user_information:
            if name in line:
                print(f"Information for {name} found: {line.strip()} ")
# Ask user if want to input a name again, exit if not