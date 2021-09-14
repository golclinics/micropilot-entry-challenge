//Author: Manav R. Patel ~ patelmanav1803@gmail.com
#include <iostream>
using namespace std;

//--Function to count number of zeros--
int countZeros(int arr[], int size){
  int count = 0;
  int temp;
  int number = size;

//--Sort the array--
  for(int j=1; j<number; j++){ 
			  temp = arr[j]; 
				int i=j;
				while(i>0 && arr[i-1] >= temp){
					arr[i] = arr[i-1];
					--i;
				}
				arr[i] = temp;
	}
// Count the number of zeros in the array
  for (int i=0; i<number; i++){
    if(arr[i]==0) //--Increment if 0 is found--
      count++; 
  }
  return count; //--Returns the number of zeros--
}

int main(){

  int number;
  int arr[5];
  
  //--Prompt user for number of digits--
  cout << "Number of digits: ";
  cin >> number;

  //--Prompt user to add the numbers
  cout << "Enter the numbers: ";
  for (int i=0; i<number; i++){
    cin >> arr[i];
  }

  //--Pass values to function countZero and display number of zeros -- 
  cout << "\nNumber of zero is: " << countZeros(arr, number) << endl;

  return 0;
}
