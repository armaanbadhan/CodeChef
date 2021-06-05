#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
ll t;
cin>>t;
while(t--)
{
ll x1,y1,x2,y2;
cin>>x1>>y1>>x2>>y2;

ll dp[x2][y2];


ll sum=0;


dp[0][0]=1;

ll sum1=0;
for(int  i=1;i<y2;i++)
{
    dp[0][i]=dp[0][i-1]+i;


}
for(int  i=1;i<x2;i++)
{

for(int  j=0;j<y2;j++)
{
dp[i][j]=dp[i-1][j]+i+j+1;

}

}


ll s=0;

for(int i=x1-1;i<x2;i++)
{
 s=s+dp[i][y1-1];
 }
 for(int i=y1;i<y2;i++)
 {
 s=s+dp[x2-1][i];
 }


 cout<<s<<endl;

 }
 return 0;
 }
