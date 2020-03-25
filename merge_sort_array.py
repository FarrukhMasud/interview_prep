from typing import List
import sys


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 or not nums2:
            return
        if m >= len(nums1):
            return
        m1 = m - 1
        n1 = n - 1
        index = len(nums1) - 1
        while m1 >= 0 or n1 >= 0:
            t1 = nums1[m1] if m1 >= 0 else -sys.maxsize - 1
            t2 = nums2[n1] if n1 >= 0 else -sys.maxsize - 1
            if t1 > t2:
                nums1[index] = t1
                m1 -= 1
            else:
                nums1[index] = t2
                n1 -= 1
            index -= 1


nums1 = [0, 0, 0]
m = 0
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
