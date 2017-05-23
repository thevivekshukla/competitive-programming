// http://codeforces.com/problemset/problem/71/A


#include <iostream>
using namespace std;

int main()
{
  int n;
  char word[100];

  cin>>n;

  while(n--)
  {
    cin>>word;

    int len=0;
    for (int i=0;i<100;i++)
    {
      if (word[i] == '\0')
        break;
      len++;
    }

    if (len>10)
      cout<<word[0]<<len-2<<word[len-1]<<endl;
    else
      cout<<word<<endl;
  }

  return 0;
}