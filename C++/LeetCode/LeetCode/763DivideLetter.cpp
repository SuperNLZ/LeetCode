#include "pch.h"
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include "763DivideLetter.h"
using namespace std;

vector<int> DivideLetter::partitionLabels(string S)
{
    unordered_map<char, int> map;
    int s_size = static_cast<int>(S.size());
    for (int i = 0; i < s_size; i++)
    { 
        map[S[i]] = i;
    }
    vector<int>result;
    int left = 0, right = 0;
    for (int i = 0; i < s_size; i++)
    {
        right = max(map[S[i]], right);
        if (i == right)
        {
            result.push_back(right - left + 1);
            left = i + 1;
            right = i + 1;
        }
    }
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << endl;
    }
    return result;
}
