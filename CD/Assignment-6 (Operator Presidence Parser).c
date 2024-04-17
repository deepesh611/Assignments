#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_EXPRESSION_LENGTH 100

typedef struct {
    char data[MAX_EXPRESSION_LENGTH];
    int top;
} Stack;

void initializeStack(Stack* stack) {
    stack->top = -1;
}

void push(Stack* stack, char element) {
    if (stack->top == MAX_EXPRESSION_LENGTH - 1) {
        printf("Stack Overflow\n");
        exit(1);
    }
    stack->data[++stack->top] = element;
}

char pop(Stack* stack) {
    if (stack->top == -1) {
        printf("Stack Underflow\n");
        exit(1);
    }
    return stack->data[stack->top--];
}

char peek(Stack* stack) {
    if (stack->top == -1) {
        printf("Stack is empty\n");
        exit(1);
    }
    return stack->data[stack->top];
}

int isOperator(char token) {
    return (token == '+' || token == '-' || token == '*' || token == '/' || token == '^');
}

int getPrecedence(char operator) {
    switch (operator) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return -1;
    }
}

void parseExpression(char* expression, char* parsedExpression) {
    Stack operatorStack;
    initializeStack(&operatorStack);

    int i = 0;
    int j = 0;

    while (expression[i] != '\0') {
        if (isdigit(expression[i])) {
            parsedExpression[j++] = expression[i++];
        } else if (isOperator(expression[i])) {
            while (operatorStack.top != -1 && getPrecedence(expression[i]) <= getPrecedence(peek(&operatorStack))) {
                parsedExpression[j++] = pop(&operatorStack);
            }
            push(&operatorStack, expression[i++]);
        } else if (expression[i] == '(') {
            push(&operatorStack, expression[i++]);
        } else if (expression[i] == ')') {
            while (operatorStack.top != -1 && peek(&operatorStack) != '(') {
                parsedExpression[j++] = pop(&operatorStack);
            }
            if (operatorStack.top != -1 && peek(&operatorStack) == '(') {
                pop(&operatorStack); // Pop the '('
            }
            i++;
        } else {
            i++;
        }
    }

    while (operatorStack.top != -1) {
        parsedExpression[j++] = pop(&operatorStack);
    }

    parsedExpression[j] = '\0';
}

int main() {
    char expression[MAX_EXPRESSION_LENGTH];
    char parsedExpression[MAX_EXPRESSION_LENGTH];

    printf("Enter an expression: ");
    fgets(expression, sizeof(expression), stdin);
    expression[strcspn(expression, "\n")] = '\0';

    parseExpression(expression, parsedExpression);

    printf("Parsed Expression: %s\n", parsedExpression);

    return 0;
}