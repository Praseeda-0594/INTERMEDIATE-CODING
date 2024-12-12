// Write a program to print the factorial of a given number

#include <stdio.h>
int main() {
    int n, f = 1, i;
    printf("Enter a number: ");
    if (scanf("%d", &n) != 1) {
        printf("Invalid input. Please enter a number.\n");
        return 1;
    }
    for (i = 1; i <= n; i++) {
        f = f*i;
    }
    printf("Factorial of %d is %d\n", n, f);
}

