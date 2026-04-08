class Solution(object):
    def exist(self, board, word):
        
        def helper(x,y,nextt,visited):

            if nextt == len(word):
                return True

            if x <0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y]!=word[nextt] or (x,y) in visited:
                return False

            visited.add((x,y))
      
            found = (
                helper(x+1,y,nextt+1,visited) or 

                helper(x,y+1,nextt+1,visited) or 

                helper(x-1,y,nextt+1,visited) or 

                helper(x,y-1,nextt+1,visited)
            )

            visited.remove((x,y))

            return found


            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if helper(i,j,0,set()):
                        return True
        
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

s= Solution()
print(s.exist(board,word))
    