class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L = 0
        R = len(heights) - 1 

        temp = []

        while L < R:
            width = R - L
            height = min(heights[L], heights[R]) 
            area = width * height
             
            temp.append(area)

            # only move the pointer at the SHORTER wall
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return max(temp)