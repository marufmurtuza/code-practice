#include <stdio.h>

int factorial(int n){

    if(n==1 || n==0){

      return 1;

    }else{

      int x = (n*factorial(n-1));

      return x;

    }

}

int main(){

    int n;

    printf("Enter Number: ");

    scanf("%d",&n);

    printf("\nGiven Number: %d\n",n);

    printf("Factorial: %d\n",factorial(n));

}
