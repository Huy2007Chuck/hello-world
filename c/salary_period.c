// File: salary_period.c
// By Huy2007Chuck
// Calculates salary period 2 I guess

#include <stdio.h>

int main() {
    int wage, days, sp1, sp2;
    printf("Please enter wage:\n");
    scanf("%d", &wage);

    printf("Days worked:\n");
    scanf("%d", &days);

    printf("Salary period 1:\n");
    scanf("%d", &sp1);

    sp2 = ((wage * days) / 26) - sp1;
    printf("Salary period 2: %d\n", &sp2);

    return 0;
}
