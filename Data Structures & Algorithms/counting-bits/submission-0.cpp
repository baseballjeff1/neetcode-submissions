#import <math.h>

class Solution {
public:
    int numBits(int n) {
        if (n == 1)
            return 1;

        int result = 0;
        int i = floor(log2(n)); //# of bits to represent integer n
        
        for(int j = 0; j <= i; j++) {
            int bit = 1 << j;
            if (n & bit)
                result++;
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
