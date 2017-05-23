// http://codeforces.com/problemset/problem/158/A

#include <iostream>
using namespace std;

int main()
{
  int n, k, ar[100];

  cin>>n>>k;

  for (int i=0; i<n; i++)
    cin>>ar[i];

  int count = 0;
  int temp = ar[k-1];

  for (int i=0; i<n; i++)
    if (ar[i]>=temp && ar[i]>0)
      count++;

  cout<<count;

  return 0;
}