class Solution {
public:
    char findTheDifference(string s, string t) {
        char result = '\0';
        for (int i = 0; i < s.length(); i++) {
            char diff = s[i] ^ t[i];
            result ^= diff;
        }

        result ^= t[t.length() - 1];
        return result;
    }
};