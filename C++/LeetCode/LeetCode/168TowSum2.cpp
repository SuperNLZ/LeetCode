#include "pch.h"
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include "168TowSum2.h"
using namespace std;

vector<int> TwoSum2::twoSum(vector<int>& numbers, int target)
{
    vector<int>result;
    int num_len = static_cast<int>(numbers.size());
    int left = 0, right = num_len - 1;
    while (left < right)
    {
        int ans = numbers[left] + numbers[right];
        if (ans == target)
        {
            break;
        }
        if (ans > target)
        {
            right--;
            continue;
        }
        left++;
    }
    return vector<int>{left + 1, right + 1};
}
