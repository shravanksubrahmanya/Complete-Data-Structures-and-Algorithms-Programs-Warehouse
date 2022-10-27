/*This is a program to find out GCD of two numbers using Euclids Algorithm,
 using recursion method*/

#include<stdio.h>

int swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

// function to perform euclids method
int GCD(int num1, int num2){
    if(num2 == 0){
        return num1;
    }
    return GCD(num2, num1 % num2);
}

int main(){
    int n1, n2, rem;

    // input values
    printf("Please Enter the vales for num1 and num2 :");
    scanf("%d %d",&n1, &n2);

    // swap numbers of num1 > num2
    if(n1 > n2)
    swap(&n1, &n2);

    printf("gcd of two numbers is: %d",GCD(n1,n2));
}