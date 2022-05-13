#include<stdio.h>

int main(){
    int num1,num2,num3;
    printf("Enter three nos ");
    // scanf("%d%d%d",num1,num2,num3);
    num1=1;
    num2=2;
    num3=3;

    if(num1>num2 && num1>num3)
        printf("Greatest no is num1");
    else if(num2>num3)
        printf("Greatest no is num2");
    else
        printf("Greatest no is num3");
/*
    if (num1>num2){
        if (num1>num3)
            printf("Num1 %d is greatest no",num1);
        else
            printf("Num3 %d is greatest no",num3);
    }
    else{
        if (num2>num3)
            printf("Num2 %d is largest no",num2);
        else
            printf("Num3 %d is largest no",num3);
    }
    return 0;
    */
}