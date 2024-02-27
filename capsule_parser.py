import os
import tarfile
import gzip

def tar_extract(file_path, file_name):
    full_file_path = os.path.join(file_path, file_name)
    print("Full file path:", full_file_path)  # Check the full file path


    # Split filename and extension
    base_name, extension = os.path.splitext(file_name)

    # Remove .tar.gz extension using os.path.splitext()
    base_name = os.path.splitext(base_name)[0]
    print("Base name without extension:", base_name)

    try:
        with tarfile.open(full_file_path, "r:gz") as tar:
            tar.extractall(path=file_path)
            print("Extraction successful")
    except tarfile.TarError as e:
        print(f"Error extracting tar file: {e}")
    

    # Check if the base directory exists
    extracted_dir = os.path.join(file_path, base_name)
    if os.path.exists(extracted_dir):
        os.chdir(extracted_dir)
        print(f"Changed current directory to: {extracted_dir}")
    else:
        print(f"Directory {extracted_dir} does not exist.")

    return base_name, full_file_path, extracted_dir

def parse_logs():
    base_name, full_file_path, extracted_dir = tar_extract(file_path, file_name)
    file_folder_list = os.listdir(extracted_dir)
    list_of_files = []
    for item in file_folder_list:
        item_path = os.path.join(extracted_dir, item)
        if item.endswith('.txt'):
            continue
        else:
            item_path = os.path.join(item_path, 'dump', 'logs', 'cohesity')  # Append 'dump/logs/cohesity' to the directory path
            try:
                os.chdir(item_path)
                files_list = os.listdir()
                for each_file in files_list:
                    if each_file.endswith('.gz'):
                        gz_file_path = os.path.join(item_path, each_file)
                        with gzip.open(gz_file_path, 'rb') as f_in:
                            unzipped_file_path = gz_file_path[:-3]
                            with open(unzipped_file_path, 'wb') as f_out:
                                f_out.write(f_in.read())
                        list_of_files.append(unzipped_file_path)
                    else:
                        files = os.path.join(item_path,each_file)
                        list_of_files.append(files)
            except FileNotFoundError:
                 print(f"Directory not found: {item_path}")
    return list_of_files 

def parse_log_summary(file_path, key_search):
    files_list = parse_logs()
    info_files = []
    if files_list:
        for filename in files_list:
            if "INFO" in filename.upper():
                info_files.append(filename)
        if info_files:
            for reading_file in info_files:
                with open(reading_file, 'r', encoding='latin-1') as file:
                    try:
                        contents = file.read()
                        for keyword in key_search:
                            occurrences = contents.count(keyword)
                            if occurrences > 0:
                                lines_with_keyword = [line.strip() for line in contents.split('\n') if keyword in line]
                                with open(file_path+'/output_file.txt', 'a') as output_file:
                                    output_file.write(f'Occurrences of "{keyword}" in file "{reading_file}":\n')
                                    for line in lines_with_keyword:
                                        output_file.write(line + '\n')
                                        #print(line)
                                        print('\n')
                            else:
                                print(f'No occurrences of "{keyword}" found in file "{reading_file}".')
                    except Exception as e:
                        print(f"Error processing file '{reading_file}': {str(e)}")
        else:
            print('No INFO files found.')
    else:
        print('No files found.')

         
# file_path = "C:\\Users\\rahul.ravi\\Pictures\\CIMB- SQL Backup"
# file_name = "Timecapsule-020624-114651.tar.gz"
# key_search = ['SGGSPSUNGSQL101']
# parse_log_summary(file_path,key_search)
# print ("Search under 'Occurrences of SGGSPSUNGSQL101 in output_file.txt' ")


#Prompt the user for the file path
file_path = input("Enter the file path: ")

# Prompt the user for the file name
file_name = input("Enter the file name: ")

# Prompt the user for the search keyword(s)
key_search_input = input("Enter the search keyword(s), separated by commas if multiple: ")
while not key_search_input:
    print("Search keyword(s) are mandatory. Please provide at least one keyword.")
    key_search_input = input("Enter the search keyword(s), separated by commas if multiple: ")
key_search = key_search_input.split(',')  # Split the input string by commas to create a list

# Display the inputs
print("File Path:", file_path)
print("File Name:", file_name)
print("Key Search:", key_search)
parse_log_summary(file_path, key_search)
print (f"Search under 'Occurrences of {key_search} in output_file.txt' ")

