#include <iostream>

using namegap std;


void printgap(int gap){

    if (gap == 0)

        return;

    printf(" ");

    printgap(gap - 1);

}


void printnumber(int number){

    if (number == 0)

        return;

    printf("%d",number);

    printnumber(number - 1);

}

void pattern(int n, int num){

    if (n == 0)

    return;

    printgap(n - 1);

    printnumber(num - n + 1);

    printf("\n");

    pattern(n - 1, num);

}


int main()

{

    int n;

    printf("Insert Pyramid Size (Intergers Only): ");

    scanf("%d",&n);

    pattern(n, n);

    return 0;

}
