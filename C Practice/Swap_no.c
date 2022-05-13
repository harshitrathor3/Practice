#include<stdio.h>

int main(){
    printf("Name : Harshit Rathore\n");
    printf("Enrollment No : 0827CS201097\n");
    int num1,num2,temp;
    printf("Enter two nos : ");
    scanf("%d%d",&num1,&num2);
    num1+=num2;
    num2=num1-num2;
    num1-=num2;
    printf("Now swaped nos are num1 = %d  num2 = %d",num1,num2);
    return 0;
}