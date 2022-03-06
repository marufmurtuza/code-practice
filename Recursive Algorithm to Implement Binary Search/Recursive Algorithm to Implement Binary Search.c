#include <stdio.h>

using namespace std;

int binarysearchalgorithm(int numberlist[], int l, int h, int elementtosearch){

    if(l > h){

        return -1;

    }



    int m = (l+h)/2;

    if(elementtosearch == numberlist[m]){

        return m;

    }

    else if(elementtosearch<numberlist[m]){

        return binarysearchalgorithm(numberlist, l, m-1, elementtosearch);

    }

    else{

        return binarysearchalgorithm(numberlist, m+1, h, elementtosearch);

    }

}

int main(void){

    int numberlist[] = {90, 30, 50, 100, 70, 20, 40, 10, 60, 80};

    int elementtosearch;

    printf("Enter a numberlist to find in the array: ");

    scanf("%d", &elementtosearch );

    int n = sizeof(numberlist)/sizeof(numberlist[0]);

    int l = 0;

    int h = n - 1;

    int index = binarysearchalgorithm(numberlist, l, h, elementtosearch);

    if(index != -1){

        printf("%d is in index %d \n",elementtosearch,index);

    }else{

        printf("%d is not present in the array \n",elementtosearch);

    }

    return 0;

}