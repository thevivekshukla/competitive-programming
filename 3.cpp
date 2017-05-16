//link: http://codeforces.com/problemset/problem/71/A

#include <iostream>
using namespace std;

int main()
{
  int n;

  cin>>n;

  while (n--)
  {
    char word[101];
    int count = 0;

    cin>>word;

    for (int i=0; i<=100; i++)
    {
      if (word[i]=='\0')
        break;
      count++;
    }

    if (count>10)
    {
      cout<<word[0]<<count-2<<word[count-1]<<endl;
    }
    else
      cout<<word<<endl;
  }


  return 0;
}