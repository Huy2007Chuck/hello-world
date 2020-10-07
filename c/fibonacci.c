// File: fibonacci.c
// By Huy2007Chuck
// Prints out the fibonacci series within range from user input

#include <stdio.h>

int main() {
    int a = 1, b = 1, c, range;
    printf("How many numbers to print in Fibonacci series?\n");
    scanf("%d", &range);

    while (range > 44) {
        printf("Range limit is 44. Please try again.\n");
        scanf("%d", &range);
    }

    printf("Fibonacci series with %d terms:\n", range);
    printf("%d\n%d\n", a, b);
    for (int i = 0; i < range; i++) {
        c = a + b;
        a = b;
        b = c;
        printf("%d\n", c);
    }

    return 0;
}
