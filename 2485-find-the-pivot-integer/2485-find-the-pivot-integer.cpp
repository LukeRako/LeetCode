class Solution {
public:
    int pivotInteger(int n) {
        int total = 0;
        int newTotal = 0;

        for (int i = 1; i <= n; i++) {
            total += i;
        }

        for (int j = 1; j <= n; j++) {
            newTotal += j;
            if (newTotal == (total - newTotal + j)) {
                return j;
            }
        }

        return -1;
    }
};