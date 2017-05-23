// http://codeforces.com/problemset/problem/231/A

#include <iostream>
using namespace std;

int main()
{
  int n;

  cin>>n;

  int count = 0;

  while(n--)
  {
    int ar[3];

    cin>>ar[0];
    cin>>ar[1];
    cin>>ar[2];

    int one_count = 0;

    for (int i=0; i<3; i++)
    {
      if (ar[i]==1)
        one_count++;
    }
    if (one_count>=2)
      count++;
  }


  cout<<count;

  return 0;
}