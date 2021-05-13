#--------------------------------REcursion 00000000000000000000000000000000000000000000000000

#include <bits/stdc++.h>
using namespace std;
 
int countDer(int n)
{
  if (n == 1) 
    return 0;
  if (n == 2) 
    return 1;
 
  return (n - 1) * (countDer(n - 1) + countDer(n - 2));
}
 
int main()
{
    int n = 4;
    cout << "Count of Derangements is "
         << countDer(n);
    return 0;
}

#--------------------------------- dp --------------------------------------------------------

def countDer(n):

    der = [0 for i in range(n + 1)]

    der[1] = 0
    der[2] = 1
     
    for i in range(3, n + 1):
        der[i] = (i - 1) * (der[i - 1] +
                            der[i - 2])
         
    return der[n]
 
n = 4
print("Count of Derangements is ", countDer(n))
