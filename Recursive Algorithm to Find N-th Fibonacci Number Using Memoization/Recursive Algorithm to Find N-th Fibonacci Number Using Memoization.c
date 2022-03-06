#include <bits/stdc++.h>

using namespace std;

const int arraysize = 1000; int memoizationarray[arraysize] = {0};


int fibonacci(int NthTerm){

	if (NthTerm == 0)

  	return 0;

  if (NthTerm == 1 || NthTerm == 2)

  	return (memoizationarray[NthTerm] = 1);


	if (memoizationarray[NthTerm])

  	return memoizationarray[NthTerm];

	int x = (NthTerm & 1)? (NthTerm+1)/2 : NthTerm/2;


	memoizationarray[NthTerm] = (NthTerm & 1)? (fibonacci(x)*fibonacci(x) + fibonacci(x-1)*fibonacci(x-1))

  	: (2*fibonacci(x-1) + fibonacci(x))*fibonacci(x);

	return memoizationarray[NthTerm];

}


int main(){

	int NthTerm;

  printf("Insert the N-th term that you want to get: ");

  scanf("%d",&NthTerm );

  printf("Result: %d \n", fibonacci(NthTerm));

  return 0;

}