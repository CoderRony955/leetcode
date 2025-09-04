#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    int findClosest(int x, int y, int z)
    {
        int diffx = abs(x - z);
        int diffy = abs(y - z);

        if (diffx < diffy){
            return 1;
        }
        else if (diffy < diffx){
            return 2;
        }
        else {
            return 0;
        }
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    cout << sol.findClosest(2, 7, 4) << endl;
    cout << sol.findClosest(2, 5, 6) << endl;
    return 0;
}
