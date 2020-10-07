// File: bmi.c
// By Huy2007Chuck
// Calculates BMI from user height and weight

#include <stdio.h>

int main() {
    float height, weight, bmi;
    
    printf("Please enter your height in centimeters:\n");
    scanf("%f", &height);

    printf("Please enter your weight in kilograms:\n");
    scanf("%f", &weight);

    height /= 100;
    bmi = weight / (height * height);

    printf("Your BMI is %0.2f.\n", bmi);

    return 0;
}
