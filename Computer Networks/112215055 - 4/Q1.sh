#!/bin/bash

# Function to search for string recursively in files
search_string() {
    local search_string="$1"
    local file="$2"

    # Check if the file exists
    if [ ! -f "$file" ]; then
        echo -e "\033[0;31mError: \033[0;35m'$file'\033[0;31m does not exist\033[0m"       # Uses ANSI Codes for text coloring
        return
    fi

    # Initialize variables
    local total_occurrences=0
    local line_number=1

    # Loop through each line in the file
    while IFS= read -r line; do
        if [[ "${line,,}" == *"${search_string,,}"* ]]; then                              # Increment total occurrences if line contains search string
            ((total_occurrences++))
            echo "Line $line_number: $line"
        fi
        ((line_number++))
    done < "$file"

    # Print total occurrences
    echo -e "\n\033[0;33mTotal occurrences of \033[0;35m'$search_string'\033[0;33m in \033[0;35m'$file'\033[0;33m: \033[0;35m$total_occurrences\033[0m\n"
}


# Main script starts here

# Check if two arguments are provided
if [ $# -eq 1 ]; then
    echo -e "\n\033[0;36mSearching for \033[0;35m'$1'\033[0;36m in all files...\033[0m\n"

    # Search for string in all files recursively
    for file in $(find . -type f); do
        search_string "$1" "$file"
    done

elif [ $# -eq 2 ]; then
  echo -e "\n\033[0;36mSearching for \033[0;35m'$1'\033[0;36m in \033[0;35m'$2'\033[0;36m...\033[0m\n"
  search_string "$1" "$2"
  
else
    echo "Usage: $0 <search_string> [file_name]"
    exit 1
fi

# For a user friendly ending
sleep 1
echo -e "\033[0;32m\nPress Enter to Continue\033[0m..."
read
