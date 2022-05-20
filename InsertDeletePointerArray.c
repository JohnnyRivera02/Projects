#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>
/*
	Johnny Rivera
	CSC 362-001
	This script demonstrates the practices to iterate through an array 
	using only pointers and addresses. The code goes through each element
	in a set array given a file with text file with integers. The code will take
	each integer and add them to their given spot in the array by value, if the
	integer is the largest in the file it will be at the end of the array vice versa.
	The code will also go through each element in the array and remove the smallest number
	in the array given the amount of calls to the function.
*/

/*
	This insert function takes in the array pointer, count value, and the current number value.
	The purpose of this function is to iterate through the array using the for loop and compare
	the current value being inserted with the values inside the current populated array.
*/
void insert(int* myArray, int count, int value)
{
	int* i = myArray;
	for (i = myArray + count - 1; i >= myArray; i--)
	{
		if ((i == myArray && *i > value) || count == 1){*i = value;}
		else
		{
			if (*(i - 1) > value){*i = *(i - 1);}
			else if (*(i - 1) < value && *(i + 1) > value){*i = value;}
			else if (i == myArray + count - 1 && *(i - 1) < value){*i = value;}
		}
	}
}

/*
	This delete function takes in the array pointer and count value. The purpose of this function is
	to iterate through the array and remove the first number in the array (the smallest). This integer will be
	returned when the function is called to inform the user which number was removed from the array.
*/
int delete(int *myArray, int count)
{
	int* i = myArray;
	int value = *i;
	for(i = myArray; i < myArray + count - 1; i++)
	{
		*i = *(i + 1);
	}
	return value;
}

/*
	This print function takes in the array pointer and the count value. The purpose of this function is
	to iterate through the array and print what value at each address in the array has. This function is called for after the 
	insert function is called for so that it shows what is added to the array. 
*/
void print(int *myArray, int count)
{
	int* i = myArray;
	for (i = myArray; i < myArray + count; i++)
	{
		printf("%d ", *i);
	}
	printf("\n");
}

/*
*	This main function initializes the array and variables/data that needs to be accessed during the 
*	program. It will call the insert function as long as the text file provided has integers to add to the
*	array. It will update count and the current array that is being stored. The file gets closed after the last
*	while loop to save resources and then it will delete and print the integers that are being called for in the
*	last for loop.
*/
void main()
{
	int myArray[20];
	int current = 0;
	int count = 1;
	FILE *fr;
	fr = fopen("p3in2.txt","r");
	while (fscanf(fr,"%d", &current) != EOF)
	{
		insert(myArray, count, current);
		print(myArray, count);
		count++;
	}
	fclose(fr);
	for (int i = count - 1; i > 0; i--)
	{
		printf("DELETED VALUE: %d \n", delete(myArray, count));
		count--;
	}

	/*
	15
	14 15
	10 14 15
	9 10 14 15
	8 9 10 14 15
	7 8 9 10 14 15
	5 7 8 9 10 14 15
	4 5 7 8 9 10 14 15
	3 4 5 7 8 9 10 14 15
	1 3 4 5 7 8 9 10 14 15
	DELETED VALUE: 1
	DELETED VALUE: 3
	DELETED VALUE: 4
	DELETED VALUE: 5
	DELETED VALUE: 7
	DELETED VALUE: 8
	DELETED VALUE: 9
	DELETED VALUE: 10
	DELETED VALUE: 14
	DELETED VALUE: 15
	*/
}
