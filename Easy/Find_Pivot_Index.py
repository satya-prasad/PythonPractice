def pivotIndex(self, nums: List[int]) -> int:
    totalSum = sum(nums)
    rightSum = totalSum-nums[0]
    leftSum = 0
    if rightSum == leftSum:
        return 0
    else:
        for i in range(1,len(nums)):
            rightSum = rightSum-nums[i]
            leftSum += nums[i-1]
            if rightSum == leftSum:
                return i
        return -1
