/*#include<iostream>
using namespace std;

int main(){
    int age;
    cout<<"Enter Your Age : ";
    cin>>age;
    if (age>60)
        cout<<"You are Elder";
    else
        if(age>20)
            cout<<"You are Young";
        else
            if(age>12)
                cout<<"You are Teenager";
            else
                cout<<"You are children";
        
    return 0;

}*/
#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"enter marks";
    cin>>n;
    if(n>=65)
    {
        cout<<"first division";
    }
    else
    if(15<n<65)
    {
        cout<<"second division";
        
    }
    else
    {
        cout<<" third division";
    }

return 0;
}