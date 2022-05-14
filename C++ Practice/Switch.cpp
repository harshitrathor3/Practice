#include<iostream>
using namespace std;

int main(){
    int x=2;
    // cin>>x;
    switch(x){
        case 1 : cout<<"Value of x is 1";
                break;
        case 2 : cout<<"Value of x is 2"<<endl;
                break;
        case 3 : cout<<"Value of x is 3"<<endl;
                break;
        case 4 : cout<<"Value of x is 4";
                break;
        default : cout<<"Value of x is out of range";
                break;
    }
    return 0;
}