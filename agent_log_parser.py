####### This script check all agent INFO logs to find out #########
import os 
import zipfile
import sys


def extract_and_list_files(file_path):     
    if not os.path.exists(file_path):
        print(f"The file path '{file_path}' does not exist. Exiting...")
        sys.exit(1)
    else:
        print(f"The file path '{file_path}' is correct.")

    directory_path, file_name = os.path.split(file_path)
    file_name_without_extension = file_name[:-4]


    if os.path.isfile(file_path):
        if zipfile.is_zipfile(file_path):
            print ("Zip File exists")
            print (f"Name of the zip file is {file_name}")
    else:
        print ("Zip File doesn't exist , please give correct path")
        sys.exit(1)

    size = os.path.getsize(file_path)
    mb = size / (1024 * 1024)
    print (f'Size of the zip file is MBs is: {mb}')
    print ("extracting the zip file")
    new_directory_path = os.path.join(directory_path,file_name_without_extension)

    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(os.chdir(directory_path))
    except zipfile.BadZipFile:
        print("Error: The ZIP file is invalid or corrupted.")
    except Exception as e:
            print("An error occurred:", e)

    list_of_INFO_files = []

    if file_name_without_extension:
        extracted_zip_name = os.path.join(directory_path,file_name_without_extension)
        print (f'The extracted zip file is present in {directory_path} with name {file_name_without_extension}')
        os.chdir(extracted_zip_name)
        list_of_all_files_in_dir = os.listdir()
        for list_of_files in list_of_all_files_in_dir:
            if "INFO" in list_of_files:
                full_path_file = os.path.join(new_directory_path,list_of_files)
                list_of_INFO_files.append(full_path_file)
    print ('The num of INFO files are, TIME TO PARSE EM:', len(list_of_INFO_files))
    return list_of_INFO_files, directory_path 

def check_task_id(task_regex_id):
    list_of_INFO_files, directory_path = extract_and_list_files(file_path)
    with open(directory_path+'/output_file.txt', 'w') as output_file:
        for files in list_of_INFO_files:
            with open(files, 'r') as file:
                content = file.readlines()
                for line in content:
                    if task_regex_id in line:
                                output_file.writelines(line)

    if os.path.getsize(directory_path+'/output_file.txt') == 0:
        print(f"The file is empty which means there are no errors for {task_regex_id} .")
    else:
        print ("The file has contents , Open output_file.txt and check contents")
     
if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    id = int(input("Enter the ID: "))
    task_regex_id = 'task_id=' + str(id)
    check_task_id(task_regex_id)




