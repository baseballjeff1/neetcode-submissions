#import <math.h>

class Solution {
public:
    int numBits(int n) {
        int result = 0;

        while (n) {
            if (n & 1)
                result++;
            
            n = n >> 1;
        }

        return result;
    }

    vector<int> countBits(int n) {
        vector<int> result;
        result.push_back(0);

        for(int i = 1; i <= n; i++) {
            result.push_back(numBits(i));
        } 

        return result;
    }
};
