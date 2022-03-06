#include <iostream>

using namespace std;

void swapping(int *a, int *b){

  int temp = *a;

  *a = *b;

  *b = temp;

}

void printarray(int array[], int size){

  for (int i = 0; i < size; i++){

    printf("%d ",array[i]);

  }

}

void selectionsortalgorithm(int array[], int size){

  for(int c=0; c < size-1; c++){

    int minimumindex=c;

    for(int i=c+1; i<size; i++){

      if(array[i] < array[minimumindex])

        minimumindex = i;

    }

    swapping(&array[minimumindex], &array[c]);

  }

}


int main(){

  int list[] = {90, 30, 50, 100, 70, 20, 40, 10, 60, 80};

  int size = sizeof(list) / sizeof(list[0]);

  selectionsortalgorithm(list, size);

  printf("Array After Selection Sorting:\n");

  printarray(list, size);

}