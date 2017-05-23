// http://codeforces.com/problemset/problem/1/A

#include <iostream>
using namespace std;

int main()
{
  long long n, m, a;

  cin>>n>>m>>a;

  long long result = ((int)(n+a-1)/a)*((int)(m+a-1)/a);

  cout<<result;

  return 0;
}