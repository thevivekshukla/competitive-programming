//link: http://codeforces.com/problemset/problem/4/A


#include <iostream>
using namespace std;

int main(void)
{
  int w;
  bool flag = true;

  cin>>w;

  if (w <= 2 || w%2!=0)
  {
    flag = false;
    cout<<"NO";
  }
  else
  {
    for (int i=2; i<=w/2; i+=2)
    {
      if ((w-i)%2 == 0)
      {
        cout<<"YES";
        flag = false;
        break;
      }
    }
  }

  if (flag)
    cout<<"NO";
}