#include<iostream>
using namespace std;

int add(int,int);

int main(){
    int a,b;
    cout<<"Enter two nos : ";
    cin>>a>>b;
    cout<<add(a,b);
    return 0;
}

int add(int x,int y){
    int z= x + y;
    return z;
}
