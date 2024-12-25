// You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * mergeAlternately(char * word1, char * word2) {
    int n1 = strlen(word1);
    int n2 = strlen(word2);
    int n = n1 + n2 + 1;
    char * string = (char *)malloc(n * sizeof(char));
    int i = 0, j = 0, k = 0;

    while (i < n1 && j < n2) {
        string[k++] = word1[i++];
        string[k++] = word2[j++];
    }

    while (i < n1) {
        string[k++] = word1[i++];
    }

    while (j < n2) {
        string[k++] = word2[j++];
    }

    string[k] = '\0';
    return string;
}

int main() {
    char word1[100], word2[100];
    int result1, result2;

    printf("Enter the first string: ");
    result1 = scanf("%99s", word1); 

    printf("Enter the second string: ");
    result2 = scanf("%99s", word2);

    if (result1 != 1 || result2 != 1) {
        printf("Error reading input.\n");
        return 1;
    }

    char *mergedString = mergeAlternately(word1, word2);

    printf("Merged string: %s\n", mergedString);


    return 0;
}
