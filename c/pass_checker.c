// File: pass_checker.c
// By: Huy2007Chuck
// Checks if input password has:
// - An uppercase character
// - A number
// - A dollar sign

#include <stdio.h>
#include <ctype.h>

int main() {
    int len = 100;
    int digit = 0, upper = 0, dollar = 0;
    char pass[len];

    printf("Enter your password\n");
    scanf("%s", &pass);

    for (int i = 0; i < len; i++) {
        if (isupper(pass[i])) {
            digit = 1;
        } else if (isdigit(pass[i])) {
            upper = 1;
        } else if (pass[i] == '$') {
            dollar = 1;
        }
    }

    if ((digit == 1) && (upper == 1) && (dollar == 1)) {
        printf("Your password (%s) is safe!\n", pass);
    } else {
        printf("Your password (%s) sucks. Use another password.\n", pass);
    }

    return 0;
}
