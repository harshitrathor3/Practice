#include<iostream>
using namespace std;

class Student{
    public:
    int a,b;
    int add(int a,int b){
        int c;
        c=a+b;
        return c;
    }
    void display(){
        cout<<"Hello World!!!";
    }
};

int main(){
    Student s;
    cout<<s.add(1,2)<<endl;
    return 0;
}