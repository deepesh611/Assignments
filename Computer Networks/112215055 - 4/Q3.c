#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>    // For getcwd
#include <sys/types.h> // For stat
#include <sys/stat.h>  // For stat
#include <dirent.h>    // For opendir, readdir
#include <fcntl.h>     // For open, O_RDONLY, O_WRONLY, O_CREAT
#include <errno.h>     // For errno

#define MAX_COMMAND_LENGTH 1024
#define MAX_FILENAME_LENGTH 256
#define BUFFER_SIZE 1024

const char *root = "C:/Users/Deepesh";

// Function to display current working directory
void display_pwd(){
    char cwd[MAX_FILENAME_LENGTH];
    if (getcwd(cwd, sizeof(cwd)) != NULL){
        printf("%s\n", cwd);
    }

    else{
        perror("\033[31mgetcwd() error\033[0m");
    }
}

// Function to move a file
int mv(const char *source, const char *destination) {
    FILE *source_file = fopen(source, "rb");
    if (source_file == NULL) {
        perror("\033[31mError opening source file\033[0m");
        return -1;
    }

    FILE *dest_file = fopen(destination, "wb");
    if (dest_file == NULL) {
        perror("\033[31mError opening destination file\033[0m");
        fclose(source_file);
        return -1;
    }

    char buffer[BUFFER_SIZE];
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, BUFFER_SIZE, source_file)) > 0) {
        size_t bytes_written = fwrite(buffer, 1, bytes_read, dest_file);
        if (bytes_written != bytes_read) {
            perror("\033[31mError writing to destination file\033[0m");
            fclose(source_file);
            fclose(dest_file);
            return -1;
        }
    }

    fclose(source_file);
    fclose(dest_file);

    if (remove(source) != 0) {
        perror("\033[31mError deleting source file\033[0m");
        return -1;
    }

    return 0;
}


// Function to display the shell prompt
void display_prompt(){
    char cwd[MAX_FILENAME_LENGTH];

    if (getcwd(cwd, sizeof(cwd)) != NULL){
        // static username && hostname
        char username[256], hostname[256];
        FILE *fp = popen("whoami", "r");

        if (fp == NULL){
            perror("\033[31musername error\033[0m");
            exit(EXIT_FAILURE);
        }

        fgets(username, sizeof username, fp);
        pclose(fp);
        fp = popen("hostname", "r");
        
        if (fp == NULL){
            perror("\033[31mhostname error\033[0m");
            exit(EXIT_FAILURE);
        }

        fgets(hostname, sizeof hostname, fp);
        pclose(fp);

        // delete newline character
        strtok(username, "\n");
        strtok(hostname, "\n");
        char *name = strtok(username, "\\");
        char *secondPart = strtok(NULL, "\\");

        // Check if the current directory is within the root directory
        if (strncmp(cwd, root, strlen(root)) == 0){
            // Replace the root directory with "~" in the current directory path
            printf("\033[1m\033[32m%s@%s:\033[36m~%s> \033[0m", secondPart, hostname, cwd + strlen(root));
            // printf("\033[1m\033[32m%s@%s:\033[0m",hostname);
        }
        
        else{
            printf("\033[32m%s@%s:\033[36m~%s> \033[0m", username, hostname, cwd);
        }
    }

    else{
        perror("\033[31mgetcwd() error\033[0m");
    }
}

// Function to search for a string in a file
void search_in_file(const char *search_string, const char *filename){
    FILE *file = fopen(filename, "r");

    if (file == NULL){
        perror("\033[31mfopen() error\033[0m");
        return;
    }

    char line[MAX_COMMAND_LENGTH];
    int line_number = 1;

    while (fgets(line, sizeof(line), file) != NULL){
        if (strstr(line, search_string) != NULL){
            printf("Match found in line %d: %s", line_number, line);
        }
        line_number++;
    }

    fclose(file);
}

// Function to split a file into chunks
void split_file(const char *filename, int num_chunks){

    FILE *input_file = fopen(filename, "rb");
    if (input_file == NULL){
        perror("\033[31mError opening input file\033[0m");
        return;
    }

    fseek(input_file, 0, SEEK_END);     // Move file pointer to the end
    long file_size = ftell(input_file); // Get the size of the file
    rewind(input_file);                 // Reset file pointer to the beginning

    long chunk_size = file_size / num_chunks; // Calculate chunk size
    char output_filename[256];

    for (int i = 0; i < num_chunks; i++){
        sprintf(output_filename, "%s.part%d", filename, i + 1);
        FILE *output_file = fopen(output_filename, "wb");
        
        if (output_file == NULL){
            perror("\033[31mError opening output file\033[0m");
            fclose(input_file);
            return;
        }

        char buffer[BUFFER_SIZE];
        long bytes_written = 0;
        size_t bytes_to_write;

        while (bytes_written < chunk_size && (bytes_to_write = fread(buffer, 1, sizeof(buffer), input_file)) > 0){
            size_t bytes_written_now = fwrite(buffer, 1, bytes_to_write, output_file);
            
            if (bytes_written_now != bytes_to_write){
                perror("\033[31mError writing to output file\033[0m");
                fclose(input_file);
                fclose(output_file);
                return;
            }

            bytes_written += bytes_written_now;
        }

        fclose(output_file);
    }

    fclose(input_file);
    printf("\033[32mFile '%s' split into %d chunks successfully\n\033[0m", filename, num_chunks);
}

// Main function
int main(){
    char command[MAX_COMMAND_LENGTH];
    char arg1[MAX_COMMAND_LENGTH], arg2[MAX_COMMAND_LENGTH];

    while (1){
        display_prompt();
        fgets(command, sizeof(command), stdin);
        command[strcspn(command, "\n")] = 0; // Remove newline character

        if (strcmp(command, "pwd") == 0){
            display_pwd();
        }

        else if (strcmp(command, "exit") == 0){
            printf("\033[33m\nExiting my_shell...\n\033[0m");
            sleep(1);
            break;
        }

        else if (strcmp(command, "help") == 0){
            printf("\n\t\t\tAvailable commands:\n");
            printf("------------------------------------------------------------------------\n");
            printf("pwd                             -   Display current working directory\n");
            printf("mv <source> <destination>       -   Move/rename a file\n");
            printf("grep <search_string> <filename> -   Search for a string in a file\n");
            printf("split <filename> <num_chunks>   -   Split a file into chunks\n");
            printf("exit                            -   Exit my_shell\n");
            printf("------------------------------------------------------------------------\n");
            printf("\n");
        }

        else if (sscanf(command, "mv %s %s", arg1, arg2) == 2){
            mv(arg1, arg2);
        }

        else if (strncmp(command, "grep ", 5) == 0){
            sscanf(command, "grep %s %s", arg1, arg2);
            search_in_file(arg1, arg2);
        }

        else if (strncmp(command, "split ", 6) == 0){
            sscanf(command, "split %s %s", arg1, arg2);
            int num_chunks = atoi(arg2);
            if (num_chunks <= 0){
                printf("\033[31mError: Number of chunks must be a positive integer.\n\033[0m");
            }

            else{
                split_file(arg1, num_chunks);
            }
        }

        else{
            printf("\033[31mError: Unrecognized command:\033[0m '%s'\n", command);
        }
    }

    return EXIT_SUCCESS;
}