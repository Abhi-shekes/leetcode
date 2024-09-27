


#include<iostream>
#include<cstdio>


using namespace std;

void swap(int &a, int &b) {

    int temp = a;
    a = b;
    b = temp;

    
}

void bubbleSort(int arr[], int length) {
    for (int i = 0; i < length - 1; i++) {

        for (int j = 0; j < length - i - 1; j++) {

            if (arr[j] > arr[j + 1]) {
                printf("%d %d \n", arr[j], arr[j + 1]);
                swap(arr[j], arr[j + 1]); 
            }

        }
    }
}


