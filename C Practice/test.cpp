#include<iostream>
using namespace std;
double cos(int x,int n)
{
	static double p=1,f=1;
	if(n==0)
	return 1;
	else {
	double	r=cos(x,n-1);
		p*=(-1)*x*x;
		f*=(2*n-1)*(2*n);
		return r+p/f;
	}
}
int main()
{
	int a,b;
	cout<<"Enter the value of x and n"<<endl;
	cin>>a>>b;
	double  result=cos(a,b);
	cout<<result<<endl;
	
}