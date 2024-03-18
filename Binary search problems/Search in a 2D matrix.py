# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# solution 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Given problem has sorted rows and columns 
        # sorting rows which has rtarget element and then will find target in that row
        row = len(matrix)
        col = len(matrix[0])

        topr = 0
        botr = row - 1

        while topr <= botr:
            mrow = (topr+ botr)//2
            if target > matrix[mrow][-1]:
                topr = mrow+1
            elif target < matrix[mrow][0]:
                botr = mrow-1
            else:
                break
        # now after getting a row which has a target we can directly go for target  
        mrow = (topr + botr)// 2
        l = 0
        r = col-1
        while l <= r:
            m = (l+r)// 2
            if target < matrix[mrow][m]:
                r =  m-1
            elif target > matrix[mrow][m]:
                l = m+1
            else:
                return True
        return False

        # if target is greater than all the elements in matrix
        if not (topr <= botr):
            return False
