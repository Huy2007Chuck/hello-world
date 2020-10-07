// File: factorial.c
// By Huy2007Chuck
// Prints out factorial of user input number

#include <stdio.h>

int main() {
    int num, res = 1;
    printf("Please enter a number:\n");
    scanf("%d", &num);

    for (int i = 1; i < num + 1; i++) {
        res *= i;
    }

    printf("%d! = %d\n", num, res);

    return 0;
}
