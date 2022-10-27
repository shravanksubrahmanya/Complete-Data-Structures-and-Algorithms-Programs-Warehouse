/*This is a program to find out GCD of two numbers using Euclids Algorithm,
 using iterative method*/

#include<stdio.h>

int swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int num1, num2, rem;

    // input values
    printf("Please Enter the vales for num1 and num2 :");
    scanf("%d %d",&num1, &num2);

    // swap numbers of num1 > num2
    if(num1 > num2)
    swap(&num1, &num2);

    // loop to perform euclids method.
    while(num1 != 0){
        rem = num2 % num1;
        num2 = num1;
        num1 = rem;
    }

    printf("gcd of two numbers is: %d", num2);
}