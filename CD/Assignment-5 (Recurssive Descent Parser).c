#include <stdio.h> 
#include <string.h> 
 
#define SUCCESS 1 
#define FAILED 0 
 
int E(), Edash(), T(), Tdash(), F(); 
 
const char *cursor; 
char string[64]; 
 
int main()
{
    printf("Enter the string\n");
    scanf("%s", string);
    cursor = string;

    printf("Input          Action\n");
    printf("-------------------------------\n");

    if (E() && *cursor == '\0')
    {
        return 0;
    }
    else
    {
        printf("Error in parsing String\n");
        return 1;
    }
}

 
int E() 
{ 
    printf("%-16s E -> T E'\n", cursor); 
    if (T()) 
    { 
        if (Edash()) 
            return SUCCESS; 
        else 
            return FAILED; 
    } 
    else 
        return FAILED; 
} 
 
int Edash() 
{ 
    if (*cursor == '+') 
    { 
        printf("%-16s E' -> + T E'\n", 
cursor); 
        cursor++; 
        if (T()) 
        { 
            if (Edash()) 
                return SUCCESS; 
            else 
                return FAILED; 
        } 
        else 
            return FAILED; 
    } 
    else 
    { 
        printf("%-16s E' -> $\n", cursor); 
        return SUCCESS; 
    } 
} 
 
int T() 
{ 
    printf("%-16s T -> F T'\n", cursor); 
    if (F()) 
    { 
        if (Tdash()) 
            return SUCCESS; 
        else 
            return FAILED; 
    } 
    else 
        return FAILED; 
} 
 
int Tdash() 
{ 
    if (*cursor == '*') 
    { 
        printf("%-16s T' -> * F T'\n", 
cursor); 
        cursor++; 
        if (F()) 
        { 
            if (Tdash()) 
                return SUCCESS; 
            else 
                return FAILED; 
        } 
        else 
            return FAILED; 
    } 
    else 
    { 
        printf("%-16s T' -> $\n", cursor); 
        return SUCCESS; 
    } 
} 
 
int F() 
{ 
    if (*cursor == '(') 
    { 
        printf("%-16s F -> ( E )\n", cursor); 
        cursor++; 
        if (E()) 
        { 
            if (*cursor == ')') 
            { 
                cursor++; 
                return SUCCESS; 
            } 
            else 
                return FAILED; 
        } 
        else 
            return FAILED; 
    } 
    else if (*cursor == 'i') 
    { 
        cursor++; 
        printf("%-16s F ->i\n", cursor); 
        return SUCCESS; 
    } 
    else 
        return FAILED; 
}



