#include <iostream>

int count_zeros(int* arr, int size){
    int count = 0;
    while(size-- > 0){
        if(*arr == 0){
            count++;
        }
        arr++;
    }
    return count;
}

int main(){
    int arr[] = {1, 0, 5, 6, 0, 2};
    int size = sizeof(arr)/sizeof(arr[0]);
    std::cout << count_zeros(arr, size) << std::endl;
    return 0;
}
