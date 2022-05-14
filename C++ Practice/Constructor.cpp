#include<iostream>
using namespace std;

class Student{
    public:
    int a,b;
    Student(){
        a=20;
        b=30;
        cout<<a<<endl<<b<<endl;
    }
    
    int add(){
        int c=a+b;
        return c;
    }
   
};

int main(){
    Student s;
    cout<<s.add();
    return 0;
}