

#include<iostream>
#include<cstdio>

using namespace std

void selection(int arr[], int n)  
{  
    int i, j, small;  
      
    for (i = 0; i < n-1; i++)    
    {  
        small = i;  
          
        for (j = i+1; j < n; j++)  
        if (arr[j] < arr[small])  
            small = j;  

        int temp = arr[small];  
        arr[small] = arr[i];  
        arr[i] = temp;  
    }  

}  