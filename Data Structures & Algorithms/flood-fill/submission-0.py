class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]

        def dfs(image, r, c, color, vist):
            rows = len(image)
            cols = len(image[0])

            if (min(r, c) < 0) or r >= rows or c >= cols or (r,c) in vist:
                return 


            if image[r][c] != oldcolor:
                return 

            vist.add((r,c))
            image[r][c] = color

            dfs(image, r + 1, c, color, vist)
            dfs(image, r - 1, c, color, vist)
            dfs(image, r, c + 1, color, vist)
            dfs(image, r, c - 1, color, vist)

        dfs(image, sr, sc, color, set())

        return image