import sys
import re

# Check if the path to the .yml file is provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the path to the .yml file as a command line argument.")
    sys.exit(1)

# Get the path to the .yml file from the command line argument
file_path = sys.argv[1]

# UtilityTool Name
ascii_text="""
  _____                             __                                     ___       _   
  \_   \__ _ _ __   ___  _ __ ___  /__\ ___ _ __ ___   _____   _____ _ __ / __\ ___ | |_ 
   / /\/ _` | '_ \ / _ \| '__/ _ \/ \/// _ \ '_ ` _ \ / _ \ \ / / _ \ '__/__\/// _ \| __|
/\/ /_| (_| | | | | (_) | | |  __/ _  \  __/ | | | | | (_) \ V /  __/ | / \/  \ (_) | |_ 
\____/ \__, |_| |_|\___/|_|  \___\/ \_/\___|_| |_| |_|\___/ \_/ \___|_| \_____/\___/ \__|
       |___/                                                                             

Author: @thebinarybot
Follow me on Twitter!
"""

print(ascii_text)

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Process the lines
for i in range(len(lines)):
    line = lines[i]
    if 'api' in line and 'ignore:' in line:
        # Remove the word "ignore:" if it has a "/" after the ":"
        lines[i] = re.sub(r'ignore:', '', line)

# Save the modified content back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)

#Print OP
print("✓ SUCCESS - 'ignore:' is removed from the endpoints when followed by '/api' in the input yml file!")
