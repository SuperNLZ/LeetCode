#include "pch.h"
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include "88MergeSortedArray.h"
using namespace std;

void MergeSortedArray::merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
{
    int pos = m + n - 1;
    while (m > 0 && n > 0)
    {
        nums1[pos] = max(nums1[m - 1], nums2[n - 1]);
        if (nums1[m - 1] > nums2[n - 1])
        {
            nums1[pos] = nums1[m - 1];
            --m;
        }
        else
        {
            nums1[pos] = nums2[n - 1];
            --n;
        }
        --pos;
    }
    while (--n >= 0)
    {
        nums1[pos] = nums2[n];
        --pos;
    }
    for (int i = 0; i < nums1.size(); i++)
    {
        cout << nums1[i] << endl;
    }

}
