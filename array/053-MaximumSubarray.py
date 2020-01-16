```
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

[示例]:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

```

#方法：直接循环相加。累加的值与当前值相比，如果大于，则继续累加；如果小于，则打断累加。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        pre_res = max_res = nums[0]
        for i in range(1, len(nums)):
            pre_res = max(nums[i], pre_res+nums[i])
            max_res = max(max_res, pre_res)
        return max_res
