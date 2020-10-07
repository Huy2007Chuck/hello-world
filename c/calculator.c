// File: calculator.c
// By: Huy2007Chuck
// A simple console calculator program

#include <stdio.h>

int main() {
    float num1, num2;
    char op;

    printf("Enter first number:\n");
    scanf("%f", &num1);
    printf("Enter second number:\n");
    scanf("%f", &num2);
    printf("Enter operator (+, -, *, /):\n");
    scanf(" %c", &op);

    switch (op) {
        case '+':
            printf("%0.2f + %0.2f = %0.2f", num1, num2, num1 + num2);
            break;
        case '-':
            printf("%0.2f - %0.2f = %0.2f", num1, num2, num1 - num2);
            break;
        case '*':
            printf("%0.2f * %0.2f = %0.2f", num1, num2, num1 * num2);
            break;
        case '/':
            printf("%0.2f / %0.2f = %0.2f", num1, num2, num1 / num2);
            break;
        default:
            printf("Invalid operator \"%c\"\n", op);
    }

    return 0;
}
