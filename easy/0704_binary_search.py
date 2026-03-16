class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, mid, right = 0, len(nums) // 2, len(nums) - 1
        while right >= left:
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
            mid = (right + left) // 2
        return -1
