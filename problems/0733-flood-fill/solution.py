class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        '''
            :type image: List[List[int]]
            :type sr: int
            :type sc: int
            :type newColor: int
            :rtype: List[List[int]]
        '''
        # Get the original color of the starting pixel
        oldColor = image[sr][sc]    

        # Check if the starting pixel is already the new color
        if oldColor == color:
            return image

        # Recursive helper function to perform flood fill
        def fill(x, y):
            # Check if current position is within bounds of image
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return
            # Check if current pixel has the same color as the starting pixel
            if image[x][y] != oldColor:
                return
            # Update current pixel color to new color
            image[x][y] = color
            # Call fill function recursively for adjacent pixels
            fill(x-1, y)
            fill(x+1, y)
            fill(x, y-1)
            fill(x, y+1)

        # Call the fill function with starting position
        fill(sr, sc)

        # Return the modified image
        return image
