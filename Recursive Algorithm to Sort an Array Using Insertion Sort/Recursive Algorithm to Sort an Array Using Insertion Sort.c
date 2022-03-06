#include <iostream>

using namespace std;


void insertionsortalgorithm(int array[], int x){

	if (x <= 1)

		return;

	insertionsortalgorithm( array, x-1 );

	int k = array[x-1];

	int j = x-2;

	while (j >= 0 && array[j] > k){

		array[j+1] = array[j];

		j--;

	}

	array[j+1] = k;

}

void arrayprintfunction(int array[], int x){

	for (int i=0; i < x; i++)

	printf("Array After Using Selection Sorting:\n");

  printf("%d ",array[i]);

}

int main(){

	int array[] = {90, 30, 50, 100, 70, 20, 40, 10, 60, 80};

	int x = sizeof(array)/sizeof(array[0]);

	insertionsortalgorithm(array, x);

	arrayprintfunction(array, x);

	return 0;

}