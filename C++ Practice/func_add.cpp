#include<iostream>
using namespace std;

int add(int &x,int &y){
    int z= x+y;
    return z;
}
int main(){
    int a,b;
    cout<<"Enter two nos : ";
    cin>>a>>b;
    cout<<add(a,b);
}