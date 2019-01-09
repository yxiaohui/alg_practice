'''
◮ Problem: given two strings x and y, find the longest common subsequence (LCS) and print its length
◮ Example:
- x: ABCBDAB
- y: BDCABC
- “BCAB” is the longest subsequence found in both sequences, so
the answer is 4

◮ Define subproblems
- Let Dij be the length of the LCS of x1...i and y1...j

◮ Find the recurrence
- If xi = yj, they both contribute to the LCS

◮ Dij=Di−1,j−1+1
- Otherwise, either xi or yj does not contribute to the LCS, so one can be dropped

◮ Dij = max{Di−1,j , Di,j−1}
- Find and solve the base cases: Di0 = D0j = 0
'''
import numpy as np

def LCS(x, y):
    n = len(x)
    m = len(y)
    print(n)
    print(m)
    D = np.zeros((n+1, m+1))
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
    return D[n][m]
  
  
x = 'ABCBDAB'
y = 'BDCABC'

LCS(x, y)
