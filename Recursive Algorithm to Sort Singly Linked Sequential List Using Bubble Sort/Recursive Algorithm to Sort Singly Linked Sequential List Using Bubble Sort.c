#include <iostream>

using namespace std;

void bubblesortalgorithm(int array[], int size){

  for(int c=0; c<size; ++c){

    for(int x=0; x < size-c; ++x){

      if(array[x] > array[x+1]){


        int temp = array[x];

        array[x] = array[x+1];

        array[x+1] = temp;

      }
    }
  }
}

void printarray(int array[], int size){

  for (int x=0; x<size; ++x){

    printf("%d ",array[x]);

  }

}

int main(){

  int list[] = {90, 30, 50, 100, 70, 20, 40, 10, 60, 80};

  int size = sizeof(list) / sizeof(list[0]);

  bubblesortalgorithm(list, size);

  printf("Array After Bubble Sorting:\n");

  printarray(list, size);

}
