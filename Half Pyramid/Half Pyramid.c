#include <iostream>

using namespace std;

void printRow(int x,int i){

   if (x == 0)

      return;

    printf("%d  ",i);

   i++;

   printRow(x - 1,i);
}

void pattern(int n, int i){

   if (n == 0)

      return;

   printRow(i,1);

   printf("\n\n");

   pattern(n - 1, i + 1);
}


int main(){

   int n;

   printf("Insert Pyramid Size (Intergers Only): ");

   scanf("%d",&n);

   pattern(n, 1);

   return 0;
 }
