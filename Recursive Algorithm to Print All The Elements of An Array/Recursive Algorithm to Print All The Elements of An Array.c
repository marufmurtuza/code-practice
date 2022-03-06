#include <stdio.h>

void elements(int array[], int start, int length);

void elements(int array[], int start, int length){

    if(start >= length)

        return;

    printf("%d  ", array[start]);

    elements(array, start+1, length);

}

int main(){

    int array_size;

    printf("\nEnter your desired array size: ");

    scanf("%d",&array_size);

    printf("\n");

    int array[array_size];

    int n, i;

	  printf("Input the number of elements: ");

    scanf("%d",&n);

    printf("\n");

    for(i=0;i<n;i++){

	      printf("Enter The Element of Index %d : ",i);

	      scanf("%d",&array[i]);
	  }

    printf("\n\nElements in the array: \n\n");

    elements(array, 0, n);

    printf("\n");

    return 0;
}