#include "pch.h"
#include <iostream>
#include <algorithm>
#include "435NoOverlapSection.h"
using namespace std;

bool cmp(vector<int>a, vector<int>b)
{
    return a[1] < b[1];
}

int NoOverlapSection::eraseOverlapIntervals(vector<vector<int>>& intervals)
{
    int inter_size = static_cast<int>(intervals.size());
    if (inter_size == 0)
    {
        return 0;
    }
    sort(intervals.begin(), intervals.end(), [](vector<int>a, vector<int>b) {
        return a[1] < b[1];
    });
    int ans = 0;
    int right = intervals[0][1];
    for (int i = 1; i < inter_size; i++)
    {
        if (intervals[i][0] < right)
        {
            ans++;
        }
        else
        {
            right = intervals[i][1];
        }
    }
    cout << ans << endl;
    return ans;
}
