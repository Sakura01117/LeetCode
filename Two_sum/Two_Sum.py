class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:  
                    continue
                total = nums[i]+ nums[j]
                if total == target:
                    return [i,j]

def main():
    nums = [2,7,11,15]
    target = 9 
    sol = Solution()
    print(sol.twoSum(nums,target))

if __name__ == "__main__":
    main()

            
        
