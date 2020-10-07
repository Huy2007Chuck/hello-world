// File: grades.c
// By Huy2007Chuck
// Prints out grade for average scores from input

#include <stdio.h>

int main() {
    int numberOfScores = 0;
    float totalScore = 0, scoreEntered = 0, avg;

    printf("Enter your scores. Enter 0 when finished.\n\n");

    do {
        printf("Test: %d. Average: %0.1f\n", numberOfScores, avg);
        printf("Enter score:\n");
        scanf("%f", &scoreEntered);

        numberOfScores++;
        totalScore += scoreEntered;
        avg = totalScore / numberOfScores;
    } while (scoreEntered != 0);

    return 0;
}
