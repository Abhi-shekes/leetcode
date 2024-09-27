#include<iostream>
#include <bits/stdc++.h>

using namespace std;

int binarySearch(int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            return mid; 
        }
        else if (arr[low] == target) {
            return low; 
        }
        else if (arr[high] == target) {
            return high; 
        }
        else if (arr[mid] > target) {
            high = mid - 1; 
        }
        else {
            low = mid + 1;
        }
    }

    return -1;
}


