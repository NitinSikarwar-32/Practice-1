#include<stdio.h>
int main()
{
	int a=5,b=3,c=6,d=2;
	d=(a=a+b*c+d)&&(b=b+c*d+a);
	printf("%d %d %d %d",a,b,c,d);
	return 0;
	//a=25,b=-10,c=6,d=1
	
}
