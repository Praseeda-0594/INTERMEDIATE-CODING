// Write a program to check if the input number is prime or not

#include <stdio.h>
int main() {
    int n, i, c = 0;
    printf("Enter a number: ");
    if (scanf("%d", &n) != 1) {
        printf("Invalid input. Please enter a number.\n");
        return 1;
    }
    for (i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            c++;
        }
    }
    c++; 
    if (c > 2)
        printf("%d is not a prime number\n", n);
    else
        printf("%d is a prime number\n", n);

    return 0;
}
