#include<iostream>
using namespace std;

int main(){
    char a;
    cout<<"Enter your Grade";
    cin>>a;
    switch(a){
        case 'A' : cout<<"Your grade is A";
                    break;
        case 'B' : cout<<"Your grade is B";
                    break;
        case 'C' : cout<<"your grade is C";
                    break;
        default :  cout<<"You are Fail";
    }
}