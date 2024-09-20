#include <iostream>
const char* dgemm_desc = "Basic implementation, three-loop dgemm.";

/*
 * This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are n-by-n matrices stored in row-major format.
 * On exit, A and B maintain their input values.
 */
void 
square_dgemm(int n, double* A, double* B, double* C) 
{
    // each row of C
    for(int i = 0; i < n; i++)
        // each column of C
        for(int j = 0; j < n; j++)
            // DP each row of A and column of B into C
            for(int k = 0; k < n; k++)
                C[i*n + j] += A[i*n + k] * B[k*n + j];
}
