#include "pch.h"
#include "iostream"
#include "algorithm"
#include "605Flower.h"
using namespace std;

bool Flower::canPlaceFlowers(vector<int>& flowerbed, int n)
{
    int len = flowerbed.size();
    int pre = 0;
    for (int i = 0; i < len && n > 0;)
    {
        bool last_flag = ((i == len - 1) || (flowerbed[i + 1] == 0));
        if (flowerbed[i] == 0 && pre == 0 && last_flag)
        {
            n--;
            flowerbed[i] = 1;
        }
        pre = flowerbed[i];
        i++;
    }
    cout << n << endl;
    return n == 0;
}
