#include<iostream>
using namespace std;
struct person{
int i;
float f;
};
int main(){
person *ptr,d;
ptr=&d;
cin>>(*ptr).i;
cin>>(*ptr).f;
cout<<(*ptr).i<<endl;
cout<<(*ptr).f;
return 0;
}
