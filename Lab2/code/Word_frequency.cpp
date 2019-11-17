#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::ifstream;
using std::ofstream;
using std::istringstream;
using std::sort;
struct Record
{
	string word;
	int count;
};

class WordStatic
{
public:
	void readFile(const char *filename);
	void writeFile(const char *filename);
	static bool sortType(const Record &v1, const Record &v2)
	{
		return v1.count>v2.count;//��������
	}
	void begin_sort()
	{
		cout << "����" << _words.size() << "�����ظ�����" << endl;
		long l = 0;
		for (int i = 0; i<_words.size(); ++i)
			l += _words[i].count;
		cout << "���ʸ���Ϊ" << l << endl;
		sort(_words.begin(), _words.end(), sortType);
	}
private:
	vector<Record> _words;
};


void WordStatic::readFile(const char *filename)//c++��string���޷���Ϊopen�Ĳ���
{
	ifstream ifs(filename);//���ļ���
	if (!ifs.good())//�򿪲�����
	{
		cout << "ifstream open file error" << endl;
		return;
	}
	string line;
	int i;
	//   WordStatic sta;
	int tips = 1;
	while (getline(ifs, line))//һ�ζ�ȡһ��
	{
		tips++;
		if (tips % 500 == 0)
			cout << tips << endl;
		istringstream iss(line);//��ȡһ��
		string word;
		while (iss >> word) //ÿ���õ�һ������
		{
			for (i = 0; i<_words.size(); ++i)
			{
				if (word==_words[i].word)
				{
					++_words[i].count;
					break;
				}
			}
			if (i == _words.size())
			{
				Record record;
				record.word = word;
				record.count = 1;
				_words.push_back(record);
			}
		}
	}
}

void WordStatic::writeFile(const char *filename)//c++��string���޷���Ϊopen�Ĳ���
{
	ofstream ofs(filename);
	if (!ofs.good())
	{
		cout << "ofstream open error " << endl;
		return;
	}

	for (int i = 0; i<_words.size(); ++i)
	{
		if(_words[i].count>1)
			ofs << _words[i].word << " " << _words[i].count << endl;
	}
	ofs.close();
}

int main()
{
	WordStatic ws;
	ws.readFile("F:\\pulls3s.txt");
	ws.begin_sort();
	ws.writeFile("F:\\out3s.txt");
	return 0;
}
