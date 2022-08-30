#include "Python.h"

float _generateUniform()
{
    time_t t;
    // printf("%d\n", RAND_MAX);
    srand((unsigned)time(&t));

    long int s = rand();
    int remainder = s % 10000;
    float prob = remainder / 10000.0;

    return prob;
}
