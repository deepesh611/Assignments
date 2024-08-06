#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h>

// Custom implementation of strcasestr function
char* strcasestr(const char* haystack, const char* needle) {
    size_t len = strlen(needle);

    while (*haystack) {
        if (strncasecmp(haystack, needle, len) == 0) {
            return (char*)haystack;
        }
        haystack++;
    }
    return NULL;
}

// Recursive function to search for a string in a directory
void search_directory(char *dir_name, char *search_string) {
    DIR *dir;
    struct dirent *entry;
    char path[1024];

    // Open the directory
    if (!(dir = opendir(dir_name)))
        return;

    // Iterate through each entry in the directory
    while ((entry = readdir(dir)) != NULL) {
        if (entry->d_type == DT_DIR) {
            // Skip current and parent directory entries
            if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
                continue;
            
            // Construct the path for the subdirectory
            snprintf(path, sizeof(path), "%s/%s", dir_name, entry->d_name);
            
            // Recursively search the subdirectory
            search_directory(path, search_string);
        } 
        
        else {
            // Construct the path for the file
            snprintf(path, sizeof(path), "%s/%s", dir_name, entry->d_name);
            
            // Open the file
            FILE *file = fopen(path, "r");

            if (file != NULL) {
                char line[1024];
                int line_number = 0;
                int occurrence = 0;
                
                // Read each line of the file
                while (fgets(line, sizeof(line), file)) {
                    line_number++;

                    // Check if the line contains the search string
                    if (strcasestr(line, search_string) != NULL) {
                        printf("\033[36mFile: %s, Line: %d\n\033[0m", path, line_number);
                        occurrence++;
                    }
                }

                // Print the total number of occurrences in the file
                if (occurrence > 0) {
                    printf("\033[32mTotal occurrences in\033[0m %s\033[32m:\033[0m %d\n", path, occurrence);
                    printf("\n");
                }
                
                // Close the file
                fclose(file);
            }
        }
    }
    
    // Close the directory
    closedir(dir);
}

int main(int argc, char *argv[]) {
    // Check if the correct number of command-line arguments are provided
    if (argc < 3) {
        printf("\033[33mUsage: %s <directory> <search_string>\n\033[0m", argv[0]);
        return 1;
    }

    printf("\n");
    
    // Call the search_directory function to search for the string in the directory
    search_directory(argv[1], argv[2]);
    
    return 0;
}
