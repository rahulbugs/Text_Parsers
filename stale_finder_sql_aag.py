#!/usr/bin/python3

import os
import re
import sys

# Function to print in red
def print_in_red(text):
    print("\033[91m{}\033[00m" .format(text))

def print_in_green(text):
    print("\033[92m{}\033[00m" .format(text))

# Check if the current directory is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <current_directory>")
    sys.exit(1)

# Get the current directory from the command line arguments
current_directory = sys.argv[1]

# List all directories in the current directory
directories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

# Initialize an empty array to store directories with IP addresses
ip_directories = []

# Define a regular expression pattern to match IP addresses
ip_address_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# Filter directories that contain an IP address in their names
for directory in directories:
    if re.search(ip_address_pattern, directory):
        ip_directories.append(directory)

# Initialize a variable to track whether kStale entries are found
kstale_found = False

# Loop over each IP directory
for ip_directory in ip_directories:
    # Change directory to the IP directory
    os.chdir(os.path.join(current_directory, ip_directory, 'dump', 'logs', 'cohesity'))

    # Get the current directory path
    current_directory_path = os.getcwd()

    # List all files in the current directory
    files_in_directory = os.listdir()

    # Filter files that contain "magneto_exec*INFO*" in their names
    magneto_exec_files_in_directory = [os.path.join(current_directory_path, file) for file in files_in_directory if "magneto_exec" in file and "INFO" in file]

    # Iterate through each magneto file
    for file in magneto_exec_files_in_directory:
        with open(file, 'r', encoding='latin-1') as f:
            # Read through the file line by line
            for line in f:
                # Check if both 'kStale' and 'Task id' are in the line
                if 'kStale' in line and 'Task id' in line:
                    kstale_found = True
                    break
            if kstale_found:
                break
    if kstale_found:
        break

# Print message about setting if kStale entries are found
if kstale_found:
    print_in_red("There appears to be occurrences of kStale entries in the magneto logs. Consider setting")
    print_in_green("magneto_sql_enable_refresh_eh_before_full_inc_backup for incremental backups")
    print_in_green("and magneto_sql_enable_refresh_eh_before_log_backup for log backups.")
else:
    print("No occurrences of kStale entries found in the magneto logs.")

