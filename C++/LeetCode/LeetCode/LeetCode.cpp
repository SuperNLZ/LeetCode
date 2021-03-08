// LeetCode.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include "TestClass.h"
#include <vector>
#include <cstring>

#include "455DiliverCookie.h"
#include "135DiliverCandy.h"
#include "435NoOverlapSection.h"
#include "605Flower.h"
#include "452ArrowBullon.h"
#include "763DivideLetter.h"
#include "168TowSum2.h"
#include "88MergeSortedArray.h"

using namespace std;

int main()
{
    std::cout << "Hello World!\n"; 

    //TestClass* test = new TestClass();
    //test->PrintNum();

    //vector<int> g { 1,2,3 };
    //vector<int> s { 1, 1 };
    //DiliverCookie* cookie = new DiliverCookie();
    //cookie->findContentChildren(g, s);

    //DiliverCandy* candy = new DiliverCandy();
    //vector<int> r{ 1,1,1,1,1 };
    ////candy->candy(r);
    //
    //NoOverlapSection* section = new NoOverlapSection();
    //vector<int>s1 { 1, 2 };
    //vector<int>s2 { 2,3 };
    //vector<int>s3 { 3,4 };
    //vector<int>s4 { 1,3 };
    //
    //vector<vector<int>> se{ { 1, 2 }, { 2, 3 }, { 3, 4 }, { 1, 3 } };
    //se = {};
    ////section->eraseOverlapIntervals(se);
    //
    //Flower* flower = new Flower();
    //vector<int>f{ 1, 0, 0, 0, 0, 1 };
    //int n = 2;
    ////flower->canPlaceFlowers(f, n);
    //
    //ArrowBullon* arrow = new ArrowBullon();
    //vector<vector<int>> ab{ { 10,16}, { 2, 8 }, { 1, 6 }, { 7, 12 } };
    //ab = { { 1, 2}, { 3, 4 }, { 5, 6 }, { 7, 8 } };
    ////arrow->findMinArrowShots(ab);
    //
    //DivideLetter* letter = new DivideLetter();
    //string s_letter = "ababcbacadefegdehijhklij";
    ////letter->partitionLabels(s_letter);
    //
    //TwoSum2* two_sum = new TwoSum2();
    //vector<int> numbers = { 2, 7, 11, 15 };
    //int target = 9;
    //two_sum->twoSum(numbers, target);

    MergeSortedArray* merge_sorted_arry = new MergeSortedArray();
    vector<int>nums1 = { 0 };
    int m = 0;
    vector<int>nums2 = {1};
    int n = 1;
    merge_sorted_arry->merge(nums1, m, nums2, n);

    system("pause");
}
