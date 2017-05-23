// http://codeforces.com/problemset/problem/96/A

#include <iostream>
#include <string>
using namespace std;

int main()
{
  string str;
  cin>>str;

  int s = str.size();
  int z = str.find("0000000");
  int o = str.find("1111111");


  if (z!=-1 || o!=-1)
    cout<<"YES";
  else
    cout<<"NO";

  return 0;
}