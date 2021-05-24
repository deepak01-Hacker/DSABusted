#include <iostream>
#include <string>

using namespace std;

int T[105][105];
int F[105][105];


int main() {
	//code
	int t,n;
	string s,str,op;
	cin>>t;
	while(t--)
	{
		cin>>n;
		cin>>str;
		s=""; op="";
		for(int i=0;i<str.size();i++)
		{
			if(i%2==0)
			s+=str[i];
			else
			op+=str[i];
		}
		for(int i=0;i<105;i++)
		{
			for(int j=0;j<105;j++)
			{
				T[i][j]=0;
				F[i][j]=0;
			}
		}
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='T')
			T[i][1]=1;
			else
			F[i][1]=1;
		}
		
		for(int len=2;len<=s.size();len++)
		{
			for(int i=0;i+len-1<s.size();i++)
			{
				for(int k=1;k<=len;k++)
				{
					if(op[i+k-1]=='&')
					{
						T[i][len]= (T[i][len] + T[i][k]*T[i+k][len-k])%1003;
						F[i][len]= (F[i][len] + F[i][k]*F[i+k][len-k])%1003;
						F[i][len]= (F[i][len] + F[i][k]*T[i+k][len-k])%1003;
						F[i][len]= (F[i][len] + T[i][k]*F[i+k][len-k])%1003;
					}
					if(op[i+k-1]=='^')
					{
						T[i][len]= (T[i][len] + F[i][k]*T[i+k][len-k])%1003;
						T[i][len]= (T[i][len] + T[i][k]*F[i+k][len-k])%1003;
						F[i][len]= (F[i][len] + F[i][k]*F[i+k][len-k])%1003;
						F[i][len]= (F[i][len] + T[i][k]*T[i+k][len-k])%1003;
					}
					if(op[i+k-1]=='|')
					{
						F[i][len]= (F[i][len] + F[i][k]*F[i+k][len-k])%1003;
						T[i][len]= (T[i][len] + T[i][k]*T[i+k][len-k])%1003;
						T[i][len]= (T[i][len] + F[i][k]*T[i+k][len-k])%1003;
						T[i][len]= (T[i][len] + T[i][k]*F[i+k][len-k])%1003;
					}
				}
			}
		}
		//cout<<s<<" "<<op<<endl;
		cout<<T[0][s.size()]<<endl;
	}
	return 0;
}
