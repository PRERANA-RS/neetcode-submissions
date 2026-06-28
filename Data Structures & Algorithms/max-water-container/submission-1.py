class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        sh=0
        
        eh=len(heights)-1
        while sh<eh :
            #if eh<len(heights):
            if heights[sh]<heights[eh] :
                
                if area<heights[sh]*(eh-sh):
                    area=heights[sh]*(eh-sh)
                sh=sh+1
                
                
            else :
                if area<heights[eh]*(eh-sh):
                    area=heights[eh]*(eh-sh)
                eh=eh-1
            
                
                
            #print(area)
        return area



