class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
        pq = []  # Priority queue (min heap) to store the height differences
        for i in range(N - 1):
            diff = heights[i + 1] - heights[i]

            # If the height difference is non-positive, skip to the next iteration
            if diff <= 0:
                continue

            # Push the positive height difference onto the priority queue
            heappush(pq, diff)

            # If the number of elements in the priority queue exceeds the available ladders
            if len(pq) > ladders:
                # Use bricks for the difference and update the available bricks
                min_h = heappop(pq)
                bricks -= min_h

            # If the remaining bricks become negative, return the current index
            if bricks < 0:
                return i

        # If we reach the end of the buildings, return the last index
        return N - 1
