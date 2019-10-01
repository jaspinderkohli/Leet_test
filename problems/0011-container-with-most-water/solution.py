class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         for i,x in enumerate(height):
#             print i,x
#             max_area = []
            
#             area = i*x
#             # print area
#         area = []
#         for i in range(0,len(height)):
#             for j in range(0,len(height)):
#                 maxarea = min(height[i],height[j]) * (j-i)
#                 area.append(maxarea)
                
#         return max(area)

        i, j , maxarea= 0, len(height)-1,0
        while i<j:
            maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
            # print i
            if height[i] < height[j]:
                i+=1
            else:
                j -=1
        return maxarea
                
            
        
