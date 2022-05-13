#include<stdio.h>

int main(){
    int num;
    printf("Enter no to check positive or negative ");
    scanf("%d",&num);
    if (num>0)
        printf("Number %d is positive",num);
    else if(num<0)
        printf("Number %d is Negative number",num);
    else
        printf("Your no is zero");
}