// You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.//

#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    int min = prices[0];
    int maxprofit = 0;        

    for (int i = 0; i < pricesSize; i++) {
        int profit = prices[i] - min;

        if (profit > maxprofit) {
            maxprofit = profit;
        }
        if (prices[i] < min) {
            min = prices[i];
        }
    }

    return maxprofit;
}

int main() {
    int n;
    printf("Enter the number of days: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input. Number of days must be a positive integer.\n");
        return 1;
    }

    int prices[n];
    printf("Enter the stock prices: ");
    for (int i = 0; i < n; i++) {
        if (scanf("%d", &prices[i]) != 1) {
            printf("Invalid input. Please enter valid integers for prices.\n");
            return 1;
        }
    }

    int result = maxProfit(prices, n);
    printf("Maximum profit: %d\n", result);

    return 0;
}

