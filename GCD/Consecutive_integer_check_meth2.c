/*This is a program to find out GCD of two numbers using Consecutive integer checking Algorithm,
 using iteration method
 method 2*/

#include<stdio.h>

// to find the minimum of two numbers
int findMin(int a, int b){
    return a < b ? a : b;
}

int swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int n1, n2, min;

    // input values
    printf("Please Enter the vales for num1 and num2 :");
    scanf("%d %d",&n1, &n2);

    // find min value
    min = findMin(n1, n2);
    
    // swapping, we need to start operation with largest number
    if(n1 < n2)
    swap(&n1,&n2);

    // decrementing min valut till it devides largest no n1
    while(n1 % min != 0)
    min--;

    // decrementing min value till it divides smallest value n2
    while(n2 % min != 0)
    min--;

    // remaining minimum value is gcd
    printf("gcd of two numbers is: %d",min);
}