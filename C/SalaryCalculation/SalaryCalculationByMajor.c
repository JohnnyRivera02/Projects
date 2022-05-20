#include "header.h"

// CSC 362
// Johnny Rivera
// Spring 2022
// 03/03/2022
// This program's purpose is to calculate the starting and maximum salary per student given a file with said information. The format for data collection
// is first name, last name, major, minor, years of experience, number of honors, number of extracurricular activities, number of volunteering activities and GPA.
// It uses characters and integers for most variables with the occational doubles for calculating floating point numbers. The program is spread throughout
// 3 .c files and 1 header file with each having comments on their functions. This main program calls all the functions and prints to the console/terminal. 
// The compute.c gathers the inputted information and runs data computations with it in order to be interpretted by the user. The io.c handles the input and output
// of the code. The compute file uses the students academic and work related information to form a potential starting and maximum salary which they can obtain. 
// This program mostly computes potential salaries for students in the technology, science, and humanities field of studies. The output of these said programs is at the bottom of this file.
void main()
{
	// Initializes all variables to be used in loop and function calls.
	char fname[20], lname[20], major[20], minor[20];
	int honors, extracurricular, volunteer, years, ceiling = 0, salary = 0, bonus = 0, startSalary = 0, maxSalary = 0, allStudentStartSalary = 0, allStudentMaxSalary = 0, allTechStartSalary = 0, allTechMaxSalary = 0;
	double gpa, totalAverage, totalTechAverage;
	int students = 0;
	int techStudents = 0;

	// Configures a variable to pass a file input
	FILE* fp1;
	fp1 = fopen("p2in3-1.txt", "r");

	// Formats output text for user-friendly view
	printf("First\t\t Last\t\t Starting\t Maximum");

	// This loops through the file until the input function returns End-of-File then breaks and prints the summary of the file.
	while(input(fp1, &fname, &lname, &major, &minor, &years, &honors, &extracurricular, &volunteer, &gpa) != EOF)
	{
		// Calls the functions to gather information for the summary function.
		compute(major, minor, years, honors, extracurricular, volunteer, gpa, &ceiling, &salary, &bonus);
		range(ceiling, salary, bonus, &startSalary, &maxSalary);
		output(fname, lname, startSalary, maxSalary);
		// This function gets information from the three functions above it to keep updating the data found.
		update(&students, &techStudents, startSalary, maxSalary, &allStudentStartSalary, &allStudentMaxSalary, &allTechStartSalary, &allTechMaxSalary, major);
	}
	// Summarizes the findings and closes the file to save on resources.
	summary(students, techStudents, allStudentStartSalary, allStudentMaxSalary, allTechStartSalary, allTechMaxSalary, &totalAverage, &totalTechAverage);
	fclose(fp1);
}

//Output for p2in2-1.txt
/*
First            Last            Starting        Maximum
Token            Black           60925           91527
Kyle             Broflovski      48676           60180
Eric             Cartman         38500           48500
Rod              Flanders        49951           61455
Theresa          Gray            59575           69876
Kenny            Jones           41350           51651
Terri            Mackleberry     51850           62151
Sherri           Macklberry      51850           62151
Stan             Marsh           41425           67625
Butter           Scotch          56150           66451
Bart             Simpson         38500           68500
Lisa             Simpson         44627           57033
Bebe             Stevens         38895           46435
Allison          Taylor          56526           67729
Wendy            Testaburger     43244           54284
Ralph            Wiggum          38500           48500
Of 16 students processed and 3 tech students processed.
Average salary for all students : $54518.50
Average salary for tech students : $67417.33
*/

//Output for p2in3-1.txt
/*
First            Last            Starting        Maximum
Kamryn           Babb            55025           65627
Taylor           Mikesell        44625           74625
Denzel           Burke           59350           89651
Braxtin          Miller          37200           47200
Jacy             Sheldon         65959           96027
Zach             Harrison        48376           59278
Reid             Carrico         56000           66000
Kateria          Poole           43876           54778
Gabby            Huthcerson      66410           97380
Steele           Chambers        43425           53425
Madison          Greene          42700           73302
Paris            Johnson         51425           61425
Jack             Sawyer          50225           80827
Of 13 students processed and 4 tech students processed.
Average salary for all students : $60928.50
Average salary for tech students : $74597.12
*/
