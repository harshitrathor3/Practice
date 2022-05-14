#include<iostream>
using namespace std;

class Student{
    public:
        int a,b;
        int add(int a,int b){
            int c;
            c = a + b;
            return c;
        }
        void display(){
            cout<<"Hello"<<endl;
        }
        int sub(int a,int b){
            int d;
            d = a - b;
            return d;
        }
};

int main(){
    Student st;
    cout<<st.add(23,45)<<endl;
    cout<<st.sub(5,7)<<endl;
    st.display();
    return 0;
}