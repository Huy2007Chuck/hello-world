// File: four_nums_product.c
// By Huy2007Chuck
// Calculates products of 4 numbers from input

#include <stdio.h>

int main() {
    int a, b, c, d, res;
    printf("Please enter 4 numbers:\n");
    scanf("%d%d%d%d", &a, &b, &c, &d);
    res = a * b * c * d;
    printf("The product of %d, %d, %d, %d is %d.\n", a, b, c, d, res);

    return 0;
}
