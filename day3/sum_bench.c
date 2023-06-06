#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s <array_size>\n", argv[0]);
        return 1;
    }

    int array_size = atoi(argv[1]);

    // Allocate memory for the array
    int* array = (int*)malloc(sizeof(int) * array_size);

    // Initialize the array with random values
    srand(time(NULL));
    for (int i = 0; i < array_size; i++) {
        array[i] = rand();
    }

    // Perform the summation
    int sum = 0;
    for (int i = 0; i < array_size; i++) {
        sum += array[i];
    }

    // Print the result and elapsed time
    printf("Sum %d numbers\n", array_size);

    // Free the allocated memory
    free(array);

    return 0;
}
