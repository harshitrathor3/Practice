#include<iostream>
using namespace std;

int main(){
    char ch[50];
    cout<<"Enter the char ";
    // cin>>ch;
    cin.get(ch,50);
    cout<<"You Entered "<<ch;
    return 0;
}