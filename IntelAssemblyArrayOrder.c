#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
//Johnny Rivera
//CSC 362-001
//This code will iterate through a given array specified by a[] in main. The size of the array
//is defined in n so that when the code runs the iterations to check through the array it happens
//for the length of it. This code uses assembly code and c code to run the operations it needs to
//and print out the results to the terminal.
void main()
{
	int a[] = { 100, 99, 97, 95, 90, 87, 86, 83, 81, 77, 74, 69, 63, 50, 44, 43, 39, 31, 29, 12 }; //Populates the list with numbers.
	int n = sizeof(a)/sizeof(a[0]); //Defines the length of the array to check for
	int i, temp, location; //Initializes variables
	_asm
	{
				mov eax, 1 // Move one into eax to add below
				mov i, eax	// Set i to 1 in order to allow future array calling
		top:	mov eax, n	// Move n to eax for future comparison
				mov ebx, i	// Move i to ebx for future comparison
				cmp ebx, eax	//Compares i and n, checks to see if the number of iterations is greater than the list
				ja end		//Jumps to end of loop once the list has finished checking through, uses ja instead of jg since numbers are signed
				mov eax, i	//Moves i into eax to find the index of the current i using i - 1 * 4
				sub eax, 1	//subtracts one from i in the first operation
				mov ebx, 4	//moves 4 into a register to use in multiplication
				mul ebx	//multiplies 4 with what is in eax
				mov ecx, a[eax]	//stores the value into register ecx to store directly into temp below
				mov temp, ecx	//stores the value in the temp variable to compare later
				mov eax, i	//moves i into accumulator for operations
				sub eax, 1	//removes 1 from i to store next
				mov location, eax	//stores the outcome of the operation into location
		mid:	mov eax, location	//loads location back into eax register at the start of the while loop for comparing numbers in the array
				cmp eax, 0	//makes sure it is not zero
				jl bot	//jumps to bot if it is less than zero. Uses jl instead of jb since numbers are signed
				mov ebx, temp	//moves temp into ebx register to be used in comparison later
				sub eax, 1	//subtracts 1 from variable location, already loaded into eax from before, to find current location in array.
				mov ecx, 4	//moves number 4 into register ecx to use for multiplication
				mul ecx	//uses the register to multiply 4 to eax and find current array offset
				mov ecx, a[eax]	//stores the newly found a[location] into ecx register to compare
				cmp ecx, ebx	//compares the a[location] with variable temp to find where to place the new number
				jle bot	//jumps to bot if the new number is less than temp to find the next number to check
				add eax, 4	//adds 4 to move up one index in the array
				mov a[eax], ecx	//sets a[location + 1] to the value at a[location] to move down in the array until it is surpassed in value.
				dec location	//decreases the location variable to go down the array
				jmp mid		//jumps back to the start of the while loop
		bot:	mov ebx, temp	//moves temp into ebx register to add to a[location + 1] 
				mov eax, location	//moves location into eax register to calculate location + 1
				mov ecx, 4	//moves 4 into ecx register for multiplication
				mul ecx	//multiplies ecx (4) and eax (location) to find current element
				mov a[eax], ebx	//moves the temp value into the a[location + 1] element calculated.
				inc i	//increases the loop variable by 1
				jmp top	//jumps to top to loop once more
		end:		//left empty to signify nothing left to do and to exit

	}
	//This loop goes through the updated array and prints out what is needed to be sent to the terminal
	printf("ARRAY ELEMENTS: ");
	for (int i = 0; i < n; i++)
	{
		printf("%d ", a[i]);
	}

	//Run #1:  100, 99, 97, 95, 90, 87, 86, 83, 81, 77, 74, 69, 63, 50, 44, 43, 39, 31, 29, 12
	//ARRAY ELEMENTS : 12 29 31 39 43 44 50 63 69 74 77 81 83 86 87 90 95 97 99 100

	//Run #2:  123456, 342100, 87539, 606006, 443322, 198371, 99109, 88018, 707007
	//ARRAY ELEMENTS: 87539 88018 99109 123456 198371 342100 443322 606006 707007
}
