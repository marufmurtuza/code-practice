#include <iostream>

using namespace std;


int returnminimumindex(int a[], int l1, int l2){

	if (l1 == l2)

		return l1;

	int x = returnminimumindex(a, l1 + 1, l2);

	return (a[l1] < a[x])? l1 : x;

}


void selectionsortalgorithm(int a[], int n, int index = 0){

	if (index == n)

	return;

	int x = returnminimumindex(a, index, n-1);

	if (x != index)

	swap(a[x], a[index]);

	selectionsortalgorithm(a, n, index + 1);

}

int main(){

	int array[] = {90, 30, 50, 100, 70, 20, 40, 10, 60, 80};

	int n = sizeof(array)/sizeof(array[0]);

	selectionsortalgorithm(array, n);

	for (int l1 = 0; l1<n ; l1++)

		printf("Array After Using Selection Sorting:\n");

		printf("%d ",array[l1]);

	return 0;
}