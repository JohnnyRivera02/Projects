#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
// CONSTANTS
#define HIGH_GPA 3.25
#define LOW_GPA 2.50
#define ACTIVITY_THRESHOLD 4
#define ACTIVITY_BONUS 451
#define TECH_BONUS 5200
#define HUMANITIES_BONUS -2500
#define EXPERIENCE_THRESHOLD 2

// Prototypes
// main.c 
void main();

// io.c
int input(FILE*, char*, char*, char*, char*, int*, int*, int*, int*, double*);
int output(char*, char*, int*, int*);
void summary(int, int, int, int, int, int, double*, double*);

//compute.c
int compute(char*, char*, int, int, int, int, double, int*, int*, int*);
int range(int, int, int, int*, int*);
int isTech(char*);
int isSci(char*);
int isHum(char*);
void update(int*, int*, int, int, int*, int*, int*, int*, char*);

