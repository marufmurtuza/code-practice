#include <bits/stdc++.h>

using namespace std;

int hocBuilder(int height){

    int shedcards = 2;

    int basefloorcards = 6;

    if(height == 1){

      int numberofcards = shedcards + basefloorcards;

      printf("Required card number for a single floor house: %d" , numberofcards);

      return numberofcards;

    }else{

      int numberofcards = shedcards + basefloorcards + (height-1)*5;

      printf("Required card number for a %d floor house: %d", height, numberofcards);

      return numberofcards;

    }

}

int main(){

    int height;

    printf("Height of the building: ");

    scanf("%d",&height);

    hocBuilder(height);

    printf("\n");

}