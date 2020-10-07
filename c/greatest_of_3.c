// File: greatest_of_3.c
// By Huy2007Chuck
// Prints out the largest number of 3 input numbers

#include <stdio.h>

int main() {
    int a, b, c;
    printf("Please enter 3 numbers:\n");
    scanf("%d%d%d", &a, &b, &c);

    if (a > b) {
        if (a > c) {
            printf("%d is the largest number.\n", a);
        } else if (a < c) {
            printf("%d is the largest number.\n", c);
        }
    } else if (a < b) {
        if (b > c) {
            printf("%d is the largest number.\n", b);
        } else if (b < c) {
            printf("%d is the largest number.\n", c);
        }
    }

    return 0;
}
