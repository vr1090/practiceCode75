"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack =[]
        
        for i,h in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > h :
                pos, height = stack.pop()
                max_area = max(max_area, (i-pos) * height)
                start = pos
            
            stack.append((start,h))
        
        print(stack)
        for i, h in stack:
            max_area = max(max_area, (len(heights)-i) * h)
        
        return max_area