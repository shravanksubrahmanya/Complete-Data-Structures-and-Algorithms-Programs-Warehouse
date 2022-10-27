/*This is a program to find out GCD of two positive numbers using Middle School Algorithm,
 using iteration method*/

#include<stdio.h>

int GCD(int n1, int n2){
    int gcd = 0, min;
    if(n1 > 0 && 0 < n2){
        gcd = 1;
        // finding out minimum value
        min = n1 < n2 ? n1:n2;

        // main logic for middle school procedure
        for(int i=2; i<=min; i++)
            while((n1 % i == 0) && (n2 % i == 0)){
                n1 = n1 /i;
                n2 = n2 /i;
                gcd *= i;
            }
    }
    return gcd;
}

int main(){
    int n1, n2, min;

    // input values
    printf("Please Enter the vales for num1 and num2 :");
    scanf("%d %d",&n1, &n2);

    printf("gcd of two numbers is: %d",GCD(n1,n2));
}