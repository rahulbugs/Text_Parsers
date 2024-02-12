import os


def environment_details(file_path, file_name):
    
    full_file_path = os.path.join(file_path,file_name)
    with open(full_file_path, 'r') as file:
        file_contents = file.read()
        
    keywords_to_find = ["ORACLE_HOME", "ORACLE_SID", "ORACLE_BASE", "DBID","Parallelism is set to", "Successfully Created pfile from memory", "Recovery Manager"]

    for keyword in keywords_to_find:
        occurrences = file_contents.count(keyword)

        if occurrences > 0:
            lines_with_keyword = [line.strip() for line in file_contents.split('\n') if keyword in line]
            print(f'Lines containing "{keyword}":')
            for line in lines_with_keyword:
                print(line)
            print ('\n')



def backup_type_and_data_files(file_path, file_name):
    
    full_file_path = os.path.join(file_path,file_name)
    with open(full_file_path, 'r') as file:

        file_contents = file.read()

    keywords_to_find = ["Incremental backup detected"]
    for keyword in keywords_to_find:
        occurrences = file_contents.count(keyword)

    if occurrences > 0:
        lines_with_keyword = [line.strip() for line in file_contents.split('\n') if keyword in line]
        print(f'{keyword}":')
        for line in lines_with_keyword:
            print(line)
            print ('\n')

    validation_crosscheck = ['datafile copy file name']
    for keyword in validation_crosscheck:
        occurrences = file_contents.count(keyword)
    print ('The no of data files cross checked are : {} '.format(occurrences))

    validation_backup_files = ['input datafile file']
    for keyword in validation_backup_files:
        occurrences = file_contents.count(keyword)
    print ('The no of data files going to backup are : {}'.format(occurrences))
    
    if validation_crosscheck != validation_backup_files:
        print ('The data files cross checked and data files backed up are not the same')
    else:
        print ('The data files cross checked and data files backed up are same ')

def backup_channels_and_files(file_path, file_name):

    full_file_path = os.path.join(file_path,file_name)
    with open(full_file_path, 'r') as file:

        file_contents = file.read()

    start_backup = ["Starting backup at"]
    for keyword in start_backup:
        backup_start_time = file_contents.count(keyword)

    if backup_start_time > 0:
        lines_with_keyword = [line.strip() for line in file_contents.split('\n') if keyword in line]
        print('Start time of backups:\n')
        for line in lines_with_keyword:
            print(line)
            print ('\n')

    start_backup = ["Finished backup at"]
    for keyword in start_backup:
        backup_start_time = file_contents.count(keyword)

    if backup_start_time > 0:
        lines_with_keyword = [line.strip() for line in file_contents.split('\n') if keyword in line]
        print('Backup finished at: \n')
        for line in lines_with_keyword:
            print(line)
            print ('\n')

    
    
            
            
        
        
        

        

    
        
    
        

    
        

            
        
        
        
    
        
    

    

    




    
        
            
            

        
        
        
        
    
            
            
        

    
    

    
    
    

















file_path = 'C:\\Users\\rahul.ravi\\Pictures\\Oracle-P1-Slow backups'
file_name= 'rman_shell_hung_incr.INFO'
environment_details(file_path, file_name)
backup_type_and_data_files(file_path, file_name)
backup_channels_and_files(file_path, file_name)

            
        
        
        
    
    
    
    
    
    

