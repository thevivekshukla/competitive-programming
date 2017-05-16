//link: http://codeforces.com/problemset/problem/1/A

#include <iostream>
#include <math.h>
using namespace std;

int main(void) {

  long long int n, m, a;

  cin>>n>>m>>a;

  long long int answer = ((m+a-1)/a) * ((n+a-1)/a);

  cout<<answer;

  return 0;
}