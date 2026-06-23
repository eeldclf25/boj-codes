#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void func(const vector<string> &inputValue)
{
    int n = stoi(inputValue[0]);

    vector<int> data;
    stringstream stream(inputValue[1]);
    int value;
    while (stream >> value)
    {
        data.push_back(value);
    }

    for (int i = n - 1; i >= 0; i--)
    {
        cout << data[i];
        if (i > 0)
        {
            cout << ' ';
        }
    }
}

int main()
{
    vector<string> inputValue;

    for (string line; getline(cin, line);)
    {
        inputValue.push_back(line);
    }

    func(inputValue);

    return 0;
}
