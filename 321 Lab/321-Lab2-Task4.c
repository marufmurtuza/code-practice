#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void sort_array(int *arr, int n) {
    int i, j, temp;
    for(i=0; i<n-1; i++) {
        for(j=0; j<n-i-1; j++) {
            if(arr[j] < arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void print_odd_even(int *arr, int n) {
    int i;
    for(i=0; i<n; i++) {
        if(arr[i] % 2 == 0) {
            printf("%d is even\n", arr[i]);
        }
        else {
            printf("%d is odd\n", arr[i]);
        }
    }
}

int main(int argc, char *argv[]) {
    int n = argc - 1;
    int arr[n];
    int i;
    for(i=0; i<n; i++) {
        arr[i] = atoi(argv[i+1]);
    }

    int pid = fork();
    if(pid == 0) {
        sort_array(arr, n);
        printf("Array sorted by child process:\n");
        for(i=0; i<n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
        exit(0);
    }
    else if(pid > 0) {
        wait(NULL);
        printf("\nOdd/Even status of array by parent process:\n");
        print_odd_even(arr, n);
        printf("\n");
    }
    else {
        printf("\nFailed to create child process\n");
    }

    return 0;
}