#include <string.h>
#include <iostream>
const char* dgemm_desc = "Blocked dgemm.";

/* This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are n-by-n matrices stored in column-major format.
 * The block_size is the size of the blocks that A and B are divided into.
 * On exit, A and B maintain their input values. */
void square_dgemm_blocked(int n, int block_size, double* A, double* B, double* C) 
{   
    double blockA[block_size * block_size], blockB[block_size * block_size];
   // each row of C
   for(int i = 0; i < n; i++)
   {
        memcpy((void *)blockA, (const void *)(A + i * block_size), sizeof(double)*block_size* block_size);

        // each column of C
        for(int j = 0; j < n; j++)
        {
            double Cij = C[i+j*n];
            // DP each row of blockA and column of blockB into fast memory Cij
            for(int k = 0; k < block_size; k++)
            {
                Cij += blockA[i+k*n] * blockB[k+j*n];
            }
            C[i+j*n] = Cij;
       }
   }
}