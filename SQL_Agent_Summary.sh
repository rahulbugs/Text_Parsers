################This script helps to provide a summary of the log file#######################
echo "This script helps to provide a summary of the log file"
filename="$1"
output_file="output.txt"
node_name=$(grep  node_name $filename | awk '{ print $2 }' | tr -d '"')
environment=$(grep env_type $filename | grep -i topology_detector |awk '{ print $6}')
# Remove existing output file
rm -f "$output_file"

while read -r line; do
    #echo "Line: $line"
    
    # Extract columns using awk to print them later
    column_7=$(echo "$line" | awk '{print $7}')
    column_9=$(echo "$line" | awk '{print $9}')
    column13=$(echo "$line" | awk '{print $13}')
    column15=$(echo "$line" | awk '{print $15}')
    column26=$(echo "$line" | awk '{print $26}')
    column29=$(echo "$line" | awk '{print $29}' | tr -d ':')
    column35=$(echo "$line" |  awk '{print $35}')
    column53=$(echo "$line" |  awk '{print $53}')
    column75=$(echo "$line" |   awk '{print $75}')

    
    if [[ $line == *'Software version'* ]]; then
        echo "Agent Software version is: $column_7" >> "$output_file"
    fi
    if [[ $line == *'agent_id'* ]]; then
	echo "Agent id is: $column_9" >> "$output_file"
    fi
    if [[ $line == *'cluster_id'* ]]; then
	echo "Cluster id is : $column13" >> "$output_file"
    if [[ $line == *'cluster_incarnation_id'* ]]; then
        echo "Cluster cluster_incarnation_id is : $column15" >> "$output_file"
    fi
    if [[ $line == *'cluster_name'* ]]; then
	echo "Cluster name: $column26"  >> "$output_file"
    fi
    if [[ $line == *'allow_multiple_cohesity_clusters'* ]]; then
        echo "allow_multiple_cohesity_clusters: $column29"  >> "$output_file"
    fi
    if [[ $line == *'subcomponent'* ]]; then
	echo "Drivers  : $column35" >> "$output_file"
    fi
    if [[ $line == *'subcomponent'* ]]; then
        echo "Drivers  : $column53" >> "$output_file"
    fi
    if [[ $line == *'account'* ]]; then
        echo "Drivers  : $column75" >> "$output_file"
    fi

	break
    fi


done < "$filename"
echo "node_name is: $node_name" >> "$output_file"
echo "The environment is: $environment"
echo "Open output.txt to review information"
cat output.txt
