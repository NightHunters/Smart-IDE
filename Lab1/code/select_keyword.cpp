#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("pulls3.txt", ios::in);
	ofstream fout("memu.txt", ios::out);
	if (!fin) cout<<"can't open the file!\n";
	string str;
	while (getline(fin, str))
	{
		if (str.find("Menu", 0) != -1 || str.find("MENU", 0) != -1)
			fout << str << endl;
	}
	return 0;
}