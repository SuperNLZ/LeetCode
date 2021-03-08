#include "pch.h"
#include "455DiliverCookie.h"
#include "iostream"
#include "algorithm"
using namespace std;

int DiliverCookie::findContentChildren(vector<int>& g, vector<int>& s)
{
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int child = 0, child_len = static_cast<int>(g.size());
    int cookie = 0, cookie_len = static_cast<int>(s.size());
    while (child < child_len && cookie < cookie_len)
    {
        if (g[child] <= s[cookie])
        {
            child++;
        }
        cookie++;
    }
    //cout << "455: " << child << endl;
    return child;
}
