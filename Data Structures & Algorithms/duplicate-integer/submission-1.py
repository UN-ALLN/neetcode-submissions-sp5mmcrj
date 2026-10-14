class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        this_dict = {}
        
        for num in nums: 
            if num in this_dict: 
                return True
            else: 
                this_dict[num] = 1
        return False