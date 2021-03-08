#include "pch.h"
#include "iostream"
#include "algorithm"
#include "452ArrowBullon.h"
using namespace std;

int ArrowBullon::findMinArrowShots(vector<vector<int>>& points)
{
    int inter_size = static_cast<int>(points.size());
    if (inter_size == 0)
    {
        return 0;
    }
    sort(points.begin(), points.end(), [](vector<int>a, vector<int>b) {
        return a[1] < b[1];
    });
    int ans = 1;
    int right = points[0][1];
    //for (int i = 1; i < inter_size; i++)
    for(vector<int>p : points)
    {
        if (p[0] > right)
        {
            right = p[1];
            ans++;
        }
    }
    cout << ans << endl;
    return ans;
}
