#User function Template for python3

def rotate(mat): 
    #code here
    n = len(mat)
    m = len(mat[0])
    
    # transpose the matrix first
    for i in range(n - 1):
        for j in range(i, m):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # reverse each row now
    for i in range(n):
        mat[i].reverse()
    return mat

