// File: primes.c
// By Huy2007Chuck
// Prints prime numbers less than number from input

#include <stdio.h>

int isPrime(int n) {
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int range;
    printf("Primes range:\n");
    scanf("%d", &range);

    for (int i = 2; i < range; i++) {
        if (isPrime(i) == 1) {
            printf("%d\n", i);
        }
    }

    return 0;
}
