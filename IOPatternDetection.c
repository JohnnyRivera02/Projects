#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>


//Johnny Rivera
//CSC 362 Programming Assignment 1
//02/06/2022

//This program takes the input from the user of a text file to input from and output to. 
//The input is taken character by character and is checked logically if it is the Upper-to-lower sequence that it required.
//Upon reaching punctation it will restart the upper-to-lower sequence and also add it.
//Every first letter in the upper-to-lower sequence is capatilized and everything else is checked and set to lowercase.
//The count of input and output characters is taken and given to the user at the end to give them an overview of the process.
//This output is also shown as a percentage to show the amount of characters actually passed through this logic gate.

//This program uses stdio.h and ctype.h, primarily isupper and islower to check if the current character is lowercase or uppercase.

void main() 
{	
	//Initializes the file reader/writer variable and two string arrays for user input. These needed to be size 50 for the larger test to avoid array corruption.
	FILE *fr, *fw;
	char inputFile[50], outputFile[50], currentChar;

	//Initializes the count variables
	int isFirst = 0;
	int sequence = 0;
	int inputC = 0, outputC = 0;

	// This section asks the user for input and uses that to open the file using the full path to avoid permission issues that were encountered during testing.
	printf("Enter the full path for your file: ");
	scanf("%s", inputFile);
	
	printf("\nEnter the full path for your file: ");
	scanf("%s", outputFile);

	fr = fopen(inputFile, "r");
	fw = fopen(outputFile, "w");

	/*File read error handling in case files do not exists.*/
	if (!fr)
	{
		printf("\n FILE COULD NOT BE FOUND.");
		return -1;
	}

	//Loop to check the characters until it reaches the End of File (EOF)
	while ((currentChar = getc(fr)) != EOF)
	{
		// If the character is alphabetic is will go through this path.
		inputC++;
		if (isalpha(currentChar))
		{
			// If its the first character then it will check if its also uppercase plus add one so that every other character is lower until sequence resets.
			if ((isFirst == 0) && isupper(currentChar))
			{
				isFirst++;
				sequence++;
				outputC++;
				putc(toupper(currentChar), fw);
			}
			//Sequence uses odd and even logic to check if upper or lower is next in sequence.
			//Even is Uppercase.
			//Odd is Lowercase.
			if(isFirst == 1)
			{
				if (((sequence % 2) == 0) && isupper(currentChar))
				{
					sequence++;
					outputC++;
					putc(tolower(currentChar), fw);
				}
				if (((sequence % 2) == 1) && islower(currentChar))
				{
					sequence++;
					outputC++;
					putc(tolower(currentChar), fw);
				}
			}
		}
		//If not alphabet but is any form of punctuation then it will reset sequence and add the character.
		if (ispunct(currentChar))
		{
			isFirst = 0;
			sequence = 0;
			putc(currentChar, fw);
			outputC++;
		}
		//If not punctuation or alphabetic then just add spaces
		if (isspace(currentChar))
		{
			putc(currentChar, fw);
			outputC++;
		}
	}
	// These lines wrap up the code by getting the output to input percentage and print all the other information to the console formatted.
	float perc = ((double)outputC/ (double)inputC) * 100;
	printf("Input File: %27s\nOutput File: %27s\nNumber of Input Characters: %3d\nNumber of Ouput Characters: %3d\nPercent reduction in output: %3.2f%%", inputFile, outputFile, inputC, outputC, perc);
	fclose(fr); 
	fclose(fw);
	//**********************Input2.txt output
	/*
	  Information is not knowledge, Knowledge is not wisdom.
	  Wisdom is not truth, Truth is not beauty.
      Beauty is not love, Love is not music, Music is the best!

	  Input File: C:\\Users\\crazy\\Documents\\input2.txt
	  Output File: C:\\Users\\crazy\\Documents\\output2.txt
	  Number of Input Characters: 374
	  Number of Ouput Characters: 155
	  Percent reduction in output: 41.44%
	  */
	//**********************Input3.txt output
	/*

	Do not speak of withered trees, Of lichen strangled coverings.
	And life just barely in the leaves, It will not be undone.

	Do not speak of withered trees, Of lichen strangled coverings.
	And life just barely in the leaves, It will not be undone.

	Do not speak of what we'Ve seen, Of water choking algae.
	And dust where fountains used to be, It will not be undone.
	A wilderness unraveling, We'Ve only just begun.

	Do not speak of ice retreat, Of islands eaten by the sea.
	And industry economy, We'Ve only just begun, It will not be undone.

	Do not speak, Oh do not speak, Your tongue is dry, Your voice is weak.
	The time has passed for words to seek, It will not be undone.

	Input File: C:\\Users\\crazy\\Documents\\input3.txt
	Output File: C:\\Users\\crazy\\Documents\\output3.txt
	Number of Input Characters: 800
	Number of Ouput Characters: 673
	Percent reduction in output: 84.12%
	*/
	
}
