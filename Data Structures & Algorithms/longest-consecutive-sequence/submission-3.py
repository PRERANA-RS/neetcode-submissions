class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = sorted(nums)
        consecutive = 1
        if len(nums) < 1:
            return 0
        i = 0
        
        # We use this to remember the longest streak we find along the way
        max_streak = 1 
        
        while i < len(nums) - 1:
            # 1. Handle Duplicates: If the next number is identical, just skip it
            if num[i] == num[i+1]:
                i = i + 1
                continue
                
            # 2. Check if consecutive
            if num[i] + 1 == num[i+1]:
                consecutive = consecutive + 1
            else:
                # 3. Gap found! Record the streak and reset it
                max_streak = max(max_streak, consecutive)
                consecutive = 1
                
            i = i + 1
        
        # One last check to see if the final streak was the longest
        max_streak = max(max_streak, consecutive)
                    
        print(max_streak)
        return (max_streak)