#include <vector>

int CountZeros(std::vector<int> A) {
    int count = 0;
    for(int x : A) {
        if(x == 0) {
            count++;
        }
    }
    return count;
}

int main() {
    
    return 0;
}