class Solution:
    def findPrevSmaller(self, heights):
        stack = []
        prev_small_ele = [-1] * len(heights)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev_small_ele[i] = stack[-1]
            stack.append(i)
        
        return prev_small_ele
    
    
    def findNextSmaller(self, heights):
        stack = []
        next_small_ele = [len(heights)] * len(heights)
        
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                next_small_ele[i] = stack[-1]
            stack.append(i)
        
        return next_small_ele
    
    def largestRectangleArea(self, heights):
        prev_small_ele = self.findPrevSmaller(heights)
        next_small_ele = self.findNextSmaller(heights)
        print(prev_small_ele)
        print(next_small_ele)
        max_area = 0
        
        for i in range(len(heights)):
            width = next_small_ele[i] - prev_small_ele[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        
        return max_area
