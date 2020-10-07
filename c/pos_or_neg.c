// File: pos_or_neg.c
// By Huy2007Chuck
// Checks if input number is positive or negative

#include <stdio.h>

int main() {
    int num;
    printf("Please enter a number (can be positive or negative):\n");
    scanf("%d", &num);
    if (num < 0) {
        printf("Your number is a negative number.\n");
    } else if (num > 0) {
        printf("Your number is a positive number.\n");
    } else {
        printf("0 is not a negative nor a positive number.\n");
    }

    return 0;
}
