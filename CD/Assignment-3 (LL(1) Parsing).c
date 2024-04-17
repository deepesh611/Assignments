#include <stdio.h>
#include <stdbool.h>

#define MAX_NON_TERMINALS 10
#define MAX_TERMINALS 10

int numNonTerminals, numTerminals;
char nonTerminals[MAX_NON_TERMINALS];
char terminals[MAX_TERMINALS];
char parsingTable[MAX_NON_TERMINALS][MAX_TERMINALS][10];

void constructParsingTable() {
    // TODO: Implement the construction of the LL(1) parsing table
    // Fill in the parsingTable array based on the grammar rules and first/follow sets
    
    // Example:
    // parsingTable[0][0] = "S -> aAb";
    // parsingTable[0][1] = "S -> c";
    // parsingTable[1][0] = "A -> d";
    // parsingTable[1][1] = "A -> ε";
}

void printParsingTable() {
    printf("Parsing Table:\n");
    printf("--------------\n");
    printf("Non-Terminals: ");
    for (int i = 0; i < numNonTerminals; i++) {
        printf("%c ", nonTerminals[i]);
    }
    printf("\n");
    
    printf("Terminals: ");
    for (int i = 0; i < numTerminals; i++) {
        printf("%c ", terminals[i]);
    }
    printf("\n");
    
    printf("--------------\n");
    
    for (int i = 0; i < numNonTerminals; i++) {
        for (int j = 0; j < numTerminals; j++) {
            printf("%s\t", parsingTable[i][j]);
        }
        printf("\n");
    }
}

int main() {
    // TODO: Initialize the nonTerminals, terminals, and parsingTable arrays
    
    // Example:
    numNonTerminals = 2;
    numTerminals = 2;
    
    nonTerminals[0] = 'S';
    nonTerminals[1] = 'A';
    
    terminals[0] = 'a';
    terminals[1] = 'c';

    
    
    constructParsingTable();
    printParsingTable();
    
    return 0;
}
