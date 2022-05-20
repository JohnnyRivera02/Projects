#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
//Johnny Rivera
//CSC 362-001
//This code using c and assembly goes through the range 2 and the number provided on the top of the loop in assembly.
//The assembly code will then check for prime numbers between that range and take note of the two primes which have the largest
//distance between them (ex.23,27 distance = 6). These two prime numbers are reported at the end in the variables firstPrime and secondPrime. 
//The variable distance records the greatest distance while the lastPrime variable is used to store the current variable passing through the loop.
//It's use is to be used for comparing and find if a new range is found or not.
void main()
{
	int firstPrime = 0;
	int secondPrime = 0;
	int lastPrime = 0;
	int distance = 0;
	int max = 0;
	int i = 2;
	int j = 2;
	_asm
	{
		top:	mov eax, 1000	//Set our limit to 100, 200, 500 or the number we need.
				cmp i, eax		//check that we haven't passed our limit
				ja end			//jumps to end to exit our loop if we passed the limit
				mov j, 2		//Reset j to 2 for instances where loop iteration is more than once
		toptw:  mov eax, i		//set up our division with i / 2
				mov ebx, 2		//add our divisor to a register for future use
				mov edx, 0		//makes sure our remainder is set to zero to allow this division operation
				div ebx			//using registers here simplifies the process
				cmp j, eax		//This makes sure we haven't passed our second for loop limit
				ja next1		//proceed to the distance checking once a prime number is found.
				mov eax, i		//adds i to register for operations
				mov ebx, j		//adds j to our second register we will be using
				mov edx, 0		//reset out remainder to zero from past division to avoid errors
				div ebx			//divides the register holding i with a register holding j
				cmp edx, 0		//checks to see if the remainder of the operation is 0
				je iszero		//if it is equal to zero it will mean that we don't have a prime number
				mov eax, j		//this increments our j loop variable if it still doesn't equal 0
				add eax, 1		//this could be set up for inc j but for better observation of how inc works i chose the long way
				mov j, eax		//stores our j+1 equal to j for the loop
				jmp toptw		//jumps to the toptw loop to check for prime numbers once again.
		iszero: jmp reset		//if not a prime number just go to the end of the loop to reset and start again.
		next1:  mov eax, i		//adds i to the accumulator for operations
				mov ebx, lastPrime	//adds lastPrime to the register to perform register - register operations
				sub eax, ebx	//performs the subtration operation (eax - ebx) and stores the answers in eax
				mov distance, eax	// completes distance = i - lastPrime to find the distance between prime numbers
				mov eax, max	//moves max to accumulator 
				cmp distance, eax	//compares distance with max to see if it is a new max distance
				jbe next2		//If the current distance between primes is less than or equal to the max it will ignore it and go to setting the lastPrime variable
				mov ebx, distance	//moves distance into the ebx register to move soon
				mov max, ebx		//moves the value in ebx into max to set the new farthest distance between primes
				mov ebx, lastPrime	//moves lastPrime to the ebx register to move soon
				mov firstPrime, ebx	//moves the value in ebx to firstPrime to set the new firstPrime range where distance between primes was the greatest 
				mov ebx, i		//moves i into the ebx register to move soon
				mov secondPrime, ebx	//moves the value in ebx into secondPrime to set the new secondPrime end of range where distance between primes was the greatest
				jmp next2	//continues to our next section once everthing is updated
		next2:  mov eax, i	//moves i into our accumulator to perform a moving operation
				mov lastPrime, eax	//moves the value in eax into the lastPrime variable to set the new lastPrime to equal the previous i in the next iteration
				jmp reset	//jumps to our reset loop to restart the loop after some operations
		reset:	mov eax, i //moves i into our eax register to use in the following addition operation
				add eax, 1 //adds 1 to the eax to do i+1
				mov i, eax //stores our value back into i from our accumulator
				jmp top		//jumps to the top loop to start once more
		end:	//empty to signify nothing more to do in the loop if it reaches this point
	}
	printf("First Prime: %d \nSecond Prime: %d \nMax: %d", firstPrime, secondPrime, max);
	/*
	2 to 200:
	First Prime: 113
	Second Prime: 127
	Max: 14

	2 to 500:
	First Prime: 113
	Second Prime: 127
	Max: 14
	
	2 to 1000:
	First Prime: 887
	Second Prime: 907
	Max: 20

	2 to 5000:
	First Prime: 1327
	Second Prime: 1361
	Max: 34
	 
	2 to 100000:
	First Prime: 31397
	Second Prime: 31469
	Max: 72
	*/
}
