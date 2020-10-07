// File: exponent.c
// By Huy2007Chuck
// Calculates exponent of 2 input numbers

#include <stdio.h>
#include <math.h>

int main() {
    int x, y, res;
    printf("Enter 2 numbers:\n");
    scanf("%d%d", &x, &y);
    res = pow(x, y);
    printf("%d the power of %d is %d.\n", x, y, res);
    return 0;
}
