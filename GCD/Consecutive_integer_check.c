/*This is a program to find out GCD of two numbers using Consecutive integer checking Algorithm,
 using iteration method*/

#include<stdio.h>

// to find the minimum of two numbers
int findMin(int a, int b){
    return a < b ? a : b;
}

int main(){
    int n1, n2, min;

    // input values
    printf("Please Enter the vales for num1 and num2 :");
    scanf("%d %d",&n1, &n2);

    // find min value
    min = findMin(n1, n2);

    // we have to find the nearest minimun value which devides both numbers n1, n2
    while((n1 % min != 0) || (n2 % min != 0))
    min--;

    printf("gcd of two numbers is: %d",min);
}