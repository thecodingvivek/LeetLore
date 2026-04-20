class Solution(object):
    def solveNQueens(self, n):
        board = [["."] * n for _ in range(n)]
        result = []

        def isvalid(board, indexh, indexv): 
            for j in range(indexv):
                if board[j][indexh] == "Q":
                    return False
            
            r, c = indexv, indexh
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = indexv, indexh
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def helper(indexv):
            if indexv == n:
                result.append(["".join(row) for row in board])
    
                return

            for indexh in range(n):
                if isvalid(board, indexh, indexv):
                    board[indexv][indexh] = "Q"
                    helper(indexv + 1)
                    board[indexv][indexh] = "."  # backtrack

        helper(0)
        return result


s = Solution()
print(s.solveNQueens(4))