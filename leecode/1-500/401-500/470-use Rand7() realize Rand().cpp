#include <iostream>
using namespace std;

// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        int a = rand7();
        int b = rand7();
        while (a == 7)
            a = rand7();
        while ( b > 5)
            b = rand7();
        return (a & 1 ? 0 : 5) + b;
    }
};

// &优先级必==低
int main() {
    int a = 14;
    if ((a & 1) == 1) {
        cout << "jishu"<< endl;
    } else  if ((a & 1) == 0) {
        cout << "oushu" << endl;
    }
    system("pause");
    return 0;
}