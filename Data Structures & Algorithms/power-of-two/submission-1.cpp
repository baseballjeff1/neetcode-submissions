class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n < 0)
            return false;
        
        int result = 0;
        while (n) {
            if (n & 1)
                result++;
            n = n >> 1;
        }

        return result == 1;
    }
};