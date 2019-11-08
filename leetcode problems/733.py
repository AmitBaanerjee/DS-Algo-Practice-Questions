733. Flood Fill

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

class Solution:
    def floodFill(self, image: List[List[int]], row: int, col: int, newColor: int) -> List[List[int]]:
        def neighbours(image,i,j):
            pairs=[]
            if i>0:
                pairs.append([i-1,j])
            if i<len(image)-1:
                pairs.append([i+1,j])
            if j>0:
                pairs.append([i,j-1])
            if j<len(image[0])-1:
                pairs.append([i,j+1])
            return pairs

        def dfs(visited,image,row,col,color,sc):

            if visited[row][col]==True:
                return
            visited[row][col]=True
            if image[row][col]==sc:
                image[row][col]=color
            else: return
            for r,c in neighbours(image,row,col):
                if image[r][c]==sc:
                    dfs(visited,image,r,c,color,sc)

        visited=[[ False for i in range(len(image[0]))]for j in range(len(image))]
        starting_color=image[row][col]
        dfs(visited,image,row,col,newColor,starting_color)
        return image
