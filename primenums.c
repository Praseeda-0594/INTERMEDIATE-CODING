// Write a program to print the number of prime numbers and the prime numbers between a given range

#include <stdio.h>

int main() {
    int a, b, n, i, c, count = 0;
    printf("Enter the range (two numbers): ");

    if (scanf("%d %d", &a, &b) != 2) {
        printf("Invalid input. Please enter two numbers.\n");
        return 1;
    }

    printf("Prime numbers between %d and %d are:\n", a, b);

    for (n = a; n <= b; n++) {
        c = 0;
        for (i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                c = 1;
                break;
            }
        }
        if (n > 1 && c == 0) {
            printf("%d\n", n);
            count++;
        }
    }

    printf("Total prime numbers: %d\n", count);
    return 0;
}
