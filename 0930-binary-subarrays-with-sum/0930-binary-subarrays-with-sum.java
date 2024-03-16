class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        return helper(goal, nums) - helper(goal - 1, nums);
    }

    public int helper(int x, int[] nums) {
        if (x < 0) { return 0; }

        int left = 0;
        int res = 0;
        int currSum = 0;

        for (int right = 0; right < nums.length; right++) {
            currSum += nums[right];

            while (currSum > x) {
                currSum -= nums[left];
                left++;
            }

            res += right - left + 1;
        }
        return res;
    }
}