#!/usr/bin/python3

import os
import re

# Function to print in red
def print_in_red(text):
    print("\033[91m{}\033[00m" .format(text))

# Define a regular expression pattern to match IP addresses
ip_address_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# Get the current directory
current_directory = os.getcwd()

# List all directories in the current directory
directories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

# Initialize an empty array to store directories with IP addresses
ip_directories = []

# Filter directories that contain an IP address in their names
for directory in directories:
    if re.search(ip_address_pattern, directory):
        ip_directories.append(directory)

# Initialize an empty list to store files with "magneto_exec*INFO*" in their names
magneto_exec_files = []

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

    # Add the matching files to the list
    magneto_exec_files.extend(magneto_exec_files_in_directory)

# Iterate through each magneto file
for file in magneto_exec_files:
    with open(file, 'r', encoding='latin-1') as f:
        # Read through the file line by line
        for line_number, line in enumerate(f, start=1):
            # Check if both 'kStale' and 'Task id' are in the line
            if 'kStale' in line and 'Task id' in line:
                print_in_red("Consider applying magneto_sql_enable_refresh_eh_before_full_inc_backup for incremental backups and magneto_sql_enable_refresh_eh_before_log_backup if the metadata changesaare too frequent")
                break

