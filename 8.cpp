// http://codeforces.com/problemset/problem/282/A

#include <iostream>
using namespace std;

int main()
{
  int n;
  cin>>n;

  int value = 0;

  while(n--)
  {
    char ar[4];
    cin>>ar;

    if (ar[1]=='+')
      value++;
    else
      value--;
  }

  cout<<value;

  return 0;
}