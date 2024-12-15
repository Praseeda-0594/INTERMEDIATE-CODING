// Write a program to print all the armstrong numbers in a given range of numbers

#include <stdio.h>

int main() {
    int a, b, n, t, d, s, r;
    printf("Enter the range (two numbers): ");

    if (scanf("%d %d", &a, &b) != 2) {
        printf("Invalid input. Please enter two numbers.\n");
        return 1;
    }

    printf("Armstrong numbers between %d and %d are:\n", a, b);

    for (n = a; n <= b; n++) {
        t = n;
        s = 0;

        while (t > 0) {
            d = t % 10;
            s += d * d * d;
            t /= 10;
        }

        if (s == n)
            printf("%d\n", n);
    }

    return 0;
}
