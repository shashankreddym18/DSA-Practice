class Solution:
  def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    m = 0  
    n = 0  

    while m < len(nums1) and n < len(nums2):
      if nums1[m] == nums2[n]:
        return nums1[m]
      if nums1[m] < nums2[n]:
        m += 1
      else:
        n += 1

    return -1