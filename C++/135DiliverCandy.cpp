#include "pch.h"
#include "iostream"
#include "algorithm"
#include "135DiliverCandy.h"
using namespace std;

int DiliverCandy::candy(vector<int>& ratings)
{
    int candy_len = static_cast<int>(ratings.size());
    vector<int>candy_vec(candy_len, 1);
    for (int i = 0; i < candy_len - 1; i++)
    {
        if (ratings[i + 1] > ratings[i])
        {
            candy_vec[i + 1] = candy_vec[i] + 1;
        }
    }
     
    int ans = candy_vec[candy_len-1];
    for (int i = candy_len - 2; i >= 0; i--)
    {
        if (ratings[i] > ratings[i + 1] && candy_vec[i] <= candy_vec[i+1])
        {
            candy_vec[i] = candy_vec[i + 1] + 1;
        }
        ans += candy_vec[i];
    }
    /*int ans = 0;
    for (int i = 0; i <= candy_len - 1; i++)
    {
        ans += candy_vec[i];
    }*/
    cout << ans << endl;
    return ans;
}
