#include<iostream>
using namespace std;

class Student{
    public:
        int a,b;
        int add(int a,int b);
        void display();
};

int Student::add(int a,int b){
    int c;
    c=a+b;
    return c;
}

void Student::display(){
    cout<<"Hello World!!!"<<endl;
}

int main(){
    Student s;
    cout<<s.add(1,2)<<endl;
    s.display();
}
