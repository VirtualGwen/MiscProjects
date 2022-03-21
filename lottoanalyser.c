/*Lotto Analyser by Gwen Virtue
  An attempt to re-create a python project that I completed 
  earlier in C.
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int myTicket[3];
int testTicket[3];

int makeRandom()
{
	int randNum;
	randNum = rand() % 9 + 1;
	
	return randNum;
}

void bubble_sort(int a[], int n) {
    int i = 0, j = 0, tmp;
    for (i = 0; i < n; i++) {   // loop n times - 1 per element
        for (j = 0; j < n - i - 1; j++) { // last i elements are sorted already
            if (a[j] > a[j + 1]) {  // swop if order is broken
                tmp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = tmp;
            }
        }
    }
}

void makeTicket(int *a, int n)
{
	for(int i = 0; i < n; ++i)
	{
		a[i] = rand() % 9 + 1;
		printf("%i", i);
	}

}

int main() 
{
	srand(time(NULL));
	
	makeTicket(myTicket, 4);
	makeTicket(testTicket, 4);
	
	
	printf("Unsorted tickets:"); 
	for(int i = 0; i < 4; ++i)
	{
		printf("%d ", myTicket[i]);
	}
	printf("\n");
	
	for (int i = 0; i < 4; ++i)
	{
		printf("%d ", testTicket[i]);
	}
	printf("\n");
	
	bubble_sort(myTicket, 3);
	bubble_sort(testTicket, 3);
	
	printf("Sorted Tickets:");
	for(int i = 0; i < 4; ++i)
	{
		printf("%d ", myTicket[i]);
	}
	printf("\n");
	
	for (int i = 0; i < 4; ++i)
	{
		printf("%d ", testTicket[i]);
	}
	
}