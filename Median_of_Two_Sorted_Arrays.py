class Solution:
    def findMedianSortedArrays(self,nums1: List[int], nums2: List[int])->float:
        nums=[]
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()
        k=len(nums)
        print(f"len de la liste est : {k}")
   
        if(k % 2 ==0 ):
            medIndice = k // 2
            medElement=(nums[medIndice-1]+nums[medIndice])/2
            return medElement
        else:
            medIndice = k // 2
            medElement=nums[medIndice]
            return medElement
