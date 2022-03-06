#include<stdio.h>

int fibonacci(int n){

   if (n <= 1){

     return n;

   }else{

     int x = fibonacci(n-1) + fibonacci(n-2);

     return x;

   }

}

int main (){

  int n;

  printf("Enter Number: \n");

  scanf("%d",&n);

  printf("Result: %d", fibonacci(n));

  return 0;

}