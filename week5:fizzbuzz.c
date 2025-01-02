/* Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** fizzBuzz(int n, int* returnSize) {
    char** a = malloc(n * sizeof(char*));
    *returnSize = n;

    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            a[i - 1] = strdup("FizzBuzz");
        } else if (i % 3 == 0) {
            a[i - 1] = strdup("Fizz");
        } else if (i % 5 == 0) {
            a[i - 1] = strdup("Buzz");
        } else {
            
            a[i - 1] = malloc(12); 
            if (!a[i - 1]) {
                perror("malloc failed");
                exit(EXIT_FAILURE);
            }
            sprintf(a[i - 1], "%d", i);
        }
    }

    return a;
}

int main() {
    int n;            
    int returnSize;
    printf("Enter the value:");
    scanf( "%d", &n);

    char** result = fizzBuzz(n, &returnSize);

    printf("FizzBuzz result for n = %d:\n", n);
    for (int i = 0; i < returnSize; i++) {
        printf("%s\n", result[i]);
        free(result[i]); 
    }

    free(result);

    return 0;
}
