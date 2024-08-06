#include <stdio.h>
#include <math.h>

int main() {
        int choice,z = 1;
        double num1, num2, result;
    
        printf("Calculator Menu:\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Exponentiation\n");
        printf("6. Square Root\n");
        printf("7. Cube Root\n");
        printf("8. Factorial of a Number\n");
        printf("9. Quit\n");
        
        while (z){
        printf("Enter your choice (1-9): ");
        scanf("%d", &choice);
    
        switch (choice) {
            case 1:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                result = num1 + num2;
                printf("Result: %.2lf\n", result);
                break;
            case 2:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                result = num1 - num2;
                printf("Result: %.2lf\n", result);
                break;
            case 3:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                result = num1 * num2;
                printf("Result: %.2lf\n", result);
                break;
            case 4:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                if (num2 != 0) {
                    result = num1 / num2;
                    printf("Result: %.2lf\n", result);
                } else {
                    printf("Error: Division by zero\n");
                }
                break;
            case 5:
                printf("Enter the base number: ");
                scanf("%lf", &num1);
                printf("Enter the exponent: ");
                scanf("%lf", &num2);
                result = pow(num1, num2);
                printf("Result: %.2lf\n", result);
                break;
            case 6:
                printf("Enter a number: ");
                scanf("%lf", &num1);
                if (num1 >= 0) {
                    result = sqrt(num1);
                    printf("Result: %.2lf\n", result);
                } else {
                    printf("Error: Invalid input\n");
                }
                break;
            case 7:
                printf("Enter a number: ");
                scanf("%lf", &num1);
                result = cbrt(num1);
                printf("Result: %.2lf\n", result);
                break;
            case 8:
                printf("Enter a Number:");
                scanf("%lf", &num1);
                result = 1;
                while (num1){
                    result = result*num1;
                    num1--;
                }
                printf("Result: %.2lf\n", result);
                break;
            case 9:
                printf("Thank you For Using the Calculator\n");
                z = 0;
                break;
            default:
                printf("Error: Invalid choice\n");
                break;
        }
        }
        return 0;
    }
