mat = [[1,4],[3,2]]
start = 0
end = len(mat[0]) - 1
rows = len(mat)
cols = len(mat[0])


def maxcol(n):
    maxi = -2
    index = 0
    for i in range(len(mat)):
        if mat[i][n] > maxi:
            maxi = mat[i][n]
            index = i
    
    return index



while start<=end:
    mid = (start+end)//2
    n = maxcol(mid)

    top    = mat[n-1][mid] if n-1 >= 0 else -1
    bottom = mat[n+1][mid] if n+1 < rows else -1
    left   = mat[n][mid-1] if mid-1 >= 0 else -1
    right  = mat[n][mid+1] if mid+1 < cols else -1

    curr = mat[n][mid]

    if curr>top and curr > bottom and curr > left and curr >right:
        print(curr)
        break
    
    elif left>curr:
        end = mid - 1
    elif right > curr:
        start = mid + 1
    

