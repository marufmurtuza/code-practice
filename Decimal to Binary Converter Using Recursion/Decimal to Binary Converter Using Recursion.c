#include <stdio.h>

int converter(int dn){

    if (dn == 0){return 0;

    }else{

      return (dn%2 + 10*converter(dn/2));

    }

}


int main(){

    int dn;

    printf("\nPlease enter the decimal number that you want to convert: ");

    scanf("%d",&dn);

    printf("\n");

    printf("The Binary of %d is %d\n",dn,converter(dn));

    return 0;

}