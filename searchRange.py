class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      def find_first(arr, tar):
        if not arr:
            return -1
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < tar:
                l = mid + 1
            else:
                r = mid
        return r if nums[r] == target else -1
      
      def find_last(arr, tar):
        if not arr:
            return -1
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if arr[mid] > tar:
                r = mid - 1
            else:
                l = mid
        return l if nums[l] == target else -1
      
      return [find_first(nums, target), find_last(nums, target)]
