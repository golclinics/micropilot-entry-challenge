#include<iostream>
#include <bits/stdc++.h>

using namespace std;
int k []= {0,1,2,3,0,0,4,0,49};
int i;
int CountZeros();
int CountZeros()
	{
		int n = sizeof(k) / sizeof(k[0]);
		cout<<count(k,k +n,0);
	}
int main()
{	
	CountZeros();
}
