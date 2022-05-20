#include "header.h"
// This function takes the input of the file and collects the data into the set variables.
int input(FILE *inputf, char *fname, char *lname, char *major, char *minor, int *years, int *honors, int *extracurricular, int *volunteer, double *gpa)
{
	return fscanf(inputf, "%s %s %s %s %d %d %d %d %lf", fname, lname, major, minor, years, honors, extracurricular, volunteer, gpa);
}

// This function prints out the output of the computations for starting and maximum salary with the student's information.
int output(char *fname, char *lname, int *startSalary, int *maxSalary)
{
	printf("\n%-15s\t %-15s %-10d\t %-10d\t", fname, lname, startSalary, maxSalary);
	return 0;
}

// This function calculates the total students processed by the program, finds the average for all and tech students.
void summary(int students, int techStudents, int allStudentStartSalary, int allStudentMaxSalary, int allTechStartSalary, int allTechMaxSalary, double *totalAverage, double *totalTechAverage)
{
	// Finds total average for all students
	*totalAverage = ((double) allStudentStartSalary + (double) allStudentMaxSalary) / (2 * (double) students);
	// If tech students are presents it computes average for them.
	if (techStudents != 0)
	{
		*totalTechAverage = ((double) allTechStartSalary + (double) allTechMaxSalary) / (2 * (double) techStudents);
	}
	//Formats and prints the information to the console/terminal.
	printf("\nOf %d students processed and %d tech students processed.", students, techStudents);
	printf("\n\t Average salary for all students:  $%.2lf", *totalAverage);
	printf("\n\t Average salary for tech students: $%.2lf", *totalTechAverage);
}
