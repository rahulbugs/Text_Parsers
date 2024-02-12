###############To parse RMAN logs and show errors##############

#########Run the script from the location where RMAN logs are placed 
Error_Finder() {
    local cur_dir=$(pwd)

    # Remove existing log and Errors.txt files
    rm -f "$cur_dir"/log.out
    rm -f "$cur_dir"/Errors.txt

    #Run egrep to search for errors
    egrep 'error|Operation failed' "$cur_dir"/rman_shell_cohesity_* >> log.out 2>&1

    # Extract the last entry from log.out
    local all_entry=$(cat "$cur_dir"/log.out)
    for i in "${all_entry[@]}"
    	do
    		result=$(echo "$i" | awk -F':' '{print $1}')
	done
    for element in ${result[@]}
	do
		egrep -C 10 'error|Operation failed' "$element" >> Errors.txt 2>&1
	done
}
Error_Finder
echo "Check for errors in the logs : log.out and errors.txt"

