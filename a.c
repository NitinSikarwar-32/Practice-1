#include<stdio.h>
#include<string.h>
int main()
{
	char a[100];
	gets(a);
	int i,r=0,l=0;
	for(i=0;i<strlen(a);i++)
	{
		if(a[i]=="(")
		r++;
		else if(a[i]==")")
		l++;
	}
	if(r==l)
	printf("'True'");
	else
	printf("'False'");
}
