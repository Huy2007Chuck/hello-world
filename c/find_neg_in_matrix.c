// File: find_neg_in_matrix.c
// By: Huy2007Chuck
// Finds the first negative number of a matrix.

#include <stdio.h>

int main() {
    float matrix[3][4] = {
        {15, 46, 3.7, 6.8},
        {34, 0, -4, 67},
        {420, 69420, -69420, 0.5}
    };
    float neg = 0;

    for (int i = 0; i < 3; i++) {
        if (neg != 0)
            break;
        else {
            for (int j = 0; j < 4; j++) {
                if (matrix[i][j] < 0){
                    neg = matrix[i][j];
                    break;
                }
            }
        }
    }

    return 0;
}
