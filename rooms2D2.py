class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n = len(moveTime)
        m = len(moveTime[0])
        dp = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        heap = [(0, 0, 0, 0)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            currTime, r, c, parity = heapq.heappop(heap)
            if currTime >= dp[r][c][parity]:
                continue
            dp[r][c][parity] = currTime
            if r == n - 1 and c == m - 1:
                return currTime
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    waitTime = max(moveTime[nr][nc], currTime)
                    moveCost = 1 if parity == 0 else 2
                    arrivalTime = waitTime + moveCost
                    nextParity = 1 - parity
                    if arrivalTime < dp[nr][nc][nextParity]:
                        heapq.heappush(heap, (arrivalTime, nr, nc, nextParity))
        return -1
        
