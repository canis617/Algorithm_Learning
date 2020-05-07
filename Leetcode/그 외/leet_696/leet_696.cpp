#include <iostream>
using namespace std;

class Solution {
public:
    int countBinarySubstrings(string s) {
        char* p1;
        char* p2;
        p1 = &s[0];
        p2 = &s[0];
        p2++;
        int p_count = 1;
        int n_count = 0;
    
        while (*(p2-1) != s[s.length-1]){
            if (*p1 == *p2) {
                p_count++;
            }
            else{
                p1 = p2;
            }
        }
    }
};